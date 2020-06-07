# -*- coding: utf-8 -*-
import sys
import Adafruit_DHT
import pymysql
import time
from time import sleep
import RPi.GPIO as io

io.setmode(io.BCM)
io.setwarnings(False)
led_pin = 17
pin_trigger = 24
pin_echo = 23
gaz_pin = 27
siren_pin = 22
sokak_pin = 16
servo_pin = 21

io.setup(sokak_pin, io.OUT)
io.setup(pin_trigger, io.OUT)
io.setup(pin_echo, io.IN)
io.setup(led_pin, io.OUT)
io.setup(siren_pin, io.OUT)
io.setup(gaz_pin, io.IN)
io.setup(servo_pin, io.OUT)

p = io.PWM(servo_pin, 50)
p.start(7.5)
sleep(2)
p.stop()


def sokakac():
    io.output(sokak_pin, io.HIGH)


def sokakkapa():
    io.output(sokak_pin, io.LOW)


def camac():
    p = io.PWM(servo_pin, 50)
    p.start(2.5)
    sleep(2)

    p.stop()


def camkapat():
    p = io.PWM(servo_pin, 50)
    p.start(7.5)
    sleep(2)

    p.stop()


def alarm():
    ledkapa()

    time.sleep(0.2)
    ledyak()


def gaz():
    if (io.input(gaz_pin) <= 0):
        print("Dikkat Gaz algılandı")
        io.output(siren_pin, io.HIGH)
        alarm()
        camac()
        alarm()


    else:
        io.output(siren_pin, io.LOW)


def isisensor():
    humidity, temperature = Adafruit_DHT.read_retry(11, 26)

    print("\033c")
    print('Sicaklik={0:0.1f}*C  Nem={1:0.1f}%'.format(temperature, humidity))


def mesafe():
    io.output(pin_trigger, io.LOW)
    time.sleep(2)
    io.output(pin_trigger, io.HIGH)

    time.sleep(0.00001)

    io.output(pin_trigger, io.LOW)
    while io.input(pin_echo) == 0:
        pulse_start_time = time.time()
    while io.input(pin_echo) == 1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time

    distance = round(pulse_duration * 17150, 2)
    print("\033c")
    print("Mesafe:", distance, "cm")


def ledyak():
    io.output(led_pin, io.HIGH)


def ledkapa():
    io.output(led_pin, io.LOW)


looperCPU = 9999999999
start = time.time()

a = ''
print('Calisiyor')
while (looperCPU != 0):
    conn = pymysql.connect(host="192.168.1.34", user="emre", passwd="12345678", db="raspberrypi")
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = "SELECT * FROM `sestanima` where id=1"
    cursor.execute(query)

    data = cursor.fetchall()
    time.sleep(1)
    for row in data:

        if (row['text'] == "salonun ışıklarını aç"):
            ledyak()
        elif (row['text'] == "salonun ışıklarını kapat"):
            ledkapa()
        elif (row['text'] == "sokağın ışıklarını kapat"):
            sokakkapa()
        elif (row['text'] == "sokağın ışıklarını aç"):
            sokakac()
        elif (row['text'] == "mesafe sensörü aktif"):
            mesafe()
        elif (row['text'] == "sıcaklık sensörü aktif"):
            isisensor()
        elif (row['text'] == "camları aç"):
            if a == 'cam acildi':
                print("\033c")
                print('cam acik')
            else:
                camac()
                a = 'cam acildi'
        elif (row['text'] == "camları kapat"):
            if a == 'cam kapandi':
                print("\033c")
                print('cam kapali')
            else:
                camkapat()
                a = 'cam kapandi'

    gaz()

conn.commit()
