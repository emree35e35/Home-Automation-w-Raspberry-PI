import pymysql
import time


looperCPU = 9999999999
start = time.time()
while (looperCPU != 0):
    conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="raspberrypi")
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query = "SELECT * FROM `sestanima` where id=1"
    cursor.execute(query)

    data = cursor.fetchall()
    time.sleep(1)
    for row in data:
        print(row['text'])
        if (row['text']=="işığı aç"):
            print("acıldı")
conn.commit()