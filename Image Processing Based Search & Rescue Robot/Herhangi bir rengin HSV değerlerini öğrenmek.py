import numpy as np
import cv2

frame = cv2.imread('resim.png')	 #resim kelimesinin yerine takip etmek istediginiz rengi iceren resim dosyasinin adini giriniz

hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

print hsv   #terminala rengin HSV degerleri matrisler seklinde yazdirilacak ... rengin dusuk ve yuksek seviyeleri ogrenilir ve nesne takip koduna eklenir
