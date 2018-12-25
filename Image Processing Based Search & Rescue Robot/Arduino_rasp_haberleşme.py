import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 9600) #Burada ttyUSB0 arduino kablosunun bagladigimiz raspberry portun adidir, kullanilan USB portun adi ogrenilip degistirmek gerekebilir.

ser.write('aruino kodunda belirlenen bir degisken') #ornegin ser.write('1') 

