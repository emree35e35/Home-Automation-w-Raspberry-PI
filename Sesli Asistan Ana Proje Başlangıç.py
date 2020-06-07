#metni sese dönüştürmek için
from gtts import gTTS
import pyaudio
import speech_recognition as sr
import gtts
#sistem dosyalarını daha rahat şekilde açmak için
import os
import pymysql

#Burada kullanacağımız 2 parametre bulunuyor, Dil ve Text

r = sr.Recognizer()

#Burada ise cihaza bağlı olan mikrofondan veri almaya başlıyor,
#daha doğrusu mikrofonu dinlemeye başlıyor.
with sr.Microphone() as source:
     print("Birşeyler Söyle!")
     audio = r.listen(source)

#Bir ses sinyali geldiği anda onu google recognizer'ı ile tanımaya çalışıyor.
#Burada birçok seçeneğimiz var, Bing, Yandex vs. ama google en iyi çalışanı diyebilirim.

#Tanıdıktan sonra eğer dediğiniz şey boş bir ses değilse, yani tıkırtı vs. Dediğiniz geri döndürecek.
data = ""
try:
   data = r.recognize_google(audio, language='tr-tr')
   data= data.lower()
   print("Bunu Söyledin :" + data)
   if data=="salonun ışıklarını aç":
       print("ışıklar açıldı")
       conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="raspberrypi")
       cursor = conn.cursor(pymysql.cursors.DictCursor)

       query = "UPDATE `sestanima` SET text=%s WHERE id=1"

       val = data
       cursor.execute(query, val)
       conn.commit()

   elif data=="salonun ışıklarını kapat":
       print("ışıklar kapatıldı")
       conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="raspberrypi")
       cursor = conn.cursor(pymysql.cursors.DictCursor)

       query = "UPDATE `sestanima` SET text=%s WHERE id=1"

       val = data
       cursor.execute(query, val)
       conn.commit()
   elif data == "mesafe sensörü aktif":
       print("mesafe sensörü aktifleştirildi")
       conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="raspberrypi")
       cursor = conn.cursor(pymysql.cursors.DictCursor)

       query = "UPDATE `sestanima` SET text=%s WHERE id=1"

       val = data
       cursor.execute(query, val)
       conn.commit()
   elif data == "sıcaklık sensörü aktif":
       print("sıcaklık sensörü aktifleştirildi")
       conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="raspberrypi")
       cursor = conn.cursor(pymysql.cursors.DictCursor)

       query = "UPDATE `sestanima` SET text=%s WHERE id=1"

       val = data
       cursor.execute(query, val)
       conn.commit()
   elif data == "sokağın ışıklarını aç":
       print("Sokağın ışıkları açıldı.")
       conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="raspberrypi")
       cursor = conn.cursor(pymysql.cursors.DictCursor)

       query = "UPDATE `sestanima` SET text=%s WHERE id=1"

       val = data
       cursor.execute(query, val)
       conn.commit()
   elif data == "sokağın ışıklarını kapat":
       print("Sokağın ışıkları kapatıldı.")
       conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="raspberrypi")
       cursor = conn.cursor(pymysql.cursors.DictCursor)

       query = "UPDATE `sestanima` SET text=%s WHERE id=1"

       val = data
       cursor.execute(query, val)
       conn.commit()

   elif data == "camları aç":
       print("Camlar Açıldı")
       conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="raspberrypi")
       cursor = conn.cursor(pymysql.cursors.DictCursor)

       query = "UPDATE `sestanima` SET text=%s WHERE id=1"

       val = data
       cursor.execute(query, val)
       conn.commit()
   elif data == "camları kapat":
       print("Camlar Kapandı")
       conn = pymysql.connect(host="localhost", user="root", passwd="12345678", db="raspberrypi")
       cursor = conn.cursor(pymysql.cursors.DictCursor)

       query = "UPDATE `sestanima` SET text=%s WHERE id=1"

       val = data
       cursor.execute(query, val)
       conn.commit()
except sr.UnknownValueError:
       print("Ne dediğini anlamadım")



