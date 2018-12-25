# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np
import serial
import cv2
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

GPIO.setup(16,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

pwm1=GPIO.PWM(32,100)
pwm1.start(100)

pwm2=GPIO.PWM(33,100)
pwm2.start(100)

pwm3=GPIO.PWM(36,100)
pwm3.start(100)

pwm4=GPIO.PWM(37,100)
pwm4.start(100)

d = False

def leave(frame):
    global d
    print "dene"
    maviLower = np.array([94, 200 , 119])
    maviUpper = np.array([116, 255 , 165])		
		
	
    blurred=cv2.GaussianBlur(frame,(11,11),0)
    hsv=cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)

    mask=cv2.inRange(hsv,maviLower,maviUpper)
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)

    cnts,_=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    center= None


    if len(cnts)>0:
    	c=max(cnts,key=cv2.contourArea)
	((x,y),radius)=cv2.minEnclosingCircle(c)
		
	M = cv2.moments(c)
	center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
	
	time.sleep(0.1)
	if radius >50:
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)
            cv2.circle(frame,center,5,(0,0,255),-1)
            ser.write('2')
            d = False


# initialize the camera 
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.write('2')
time.sleep(0.1)
 
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        frame = frame.array
 
        row = frame.shape[0]
        collumn = frame.shape[1]

        #print row
        #print collumn

	rawCapture.truncate(0)

	if d == False:
            greenLower = np.array([63, 134 , 32])
            greenUpper = np.array([92, 255 , 116])	
            
            blurred=cv2.GaussianBlur(frame,(11,11),0)
            hsv=cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)

            mask=cv2.inRange(hsv,greenLower,greenUpper)
            mask=cv2.erode(mask,None,iterations=2)
            mask=cv2.dilate(mask,None,iterations=2)

            cnts,_=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            center= None


            if len(cnts)>0:
                    c=max(cnts,key=cv2.contourArea)
                    ((x,y),radius)=cv2.minEnclosingCircle(c)
                    
                    M = cv2.moments(c)
                    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                    
                    time.sleep(0.1)
                    if radius >10:
                            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)
                            cv2.circle(frame,center,5,(0,0,255),-1)
                            #print y
                            print radius

                            #time.sleep(0.1)
            
                            if x<260:
                                    #ser.write('left')
                                    print 'left'
                                    GPIO.output(32,GPIO.HIGH)
                                    GPIO.output(33,GPIO.HIGH)
                                    GPIO.output(36,GPIO.HIGH)
                                    GPIO.output(37,GPIO.HIGH)


                                    GPIO.output(11,GPIO.HIGH)
                                    GPIO.output(13,GPIO.LOW)
                                    GPIO.output(15,GPIO.LOW)
                                    GPIO.output(16,GPIO.LOW)
                                    
                                    GPIO.output(18,GPIO.HIGH)
                                    GPIO.output(22,GPIO.LOW)
                                    GPIO.output(29,GPIO.LOW)
                                    GPIO.output(31,GPIO.LOW)
                                    
                                    
                                    """time.sleep(0.20)
                                    GPIO.output(11,GPIO.LOW)
                                    GPIO.output(13,GPIO.LOW)
                                    GPIO.output(15,GPIO.LOW)
                                    GPIO.output(16,GPIO.LOW)
                                    GPIO.output(18,GPIO.LOW)
                                    GPIO.output(22,GPIO.LOW)
                                    GPIO.output(29,GPIO.LOW)
                                    GPIO.output(31,GPIO.LOW)
                                    time.sleep(0.20)"""
                                    
                            elif x>380:
                                    #ser.write('right')
                                    print 'right'
                                    GPIO.output(32,GPIO.HIGH)
                                    GPIO.output(33,GPIO.HIGH)
                                    GPIO.output(36,GPIO.HIGH)
                                    GPIO.output(37,GPIO.HIGH)

                                    GPIO.output(11,GPIO.LOW)
                                    GPIO.output(13,GPIO.LOW)
                                    GPIO.output(15,GPIO.HIGH)
                                    GPIO.output(16,GPIO.LOW)
                                    
                                    GPIO.output(18,GPIO.LOW)
                                    GPIO.output(22,GPIO.LOW)
                                    GPIO.output(29,GPIO.HIGH)
                                    GPIO.output(31,GPIO.LOW)
                                    
                                    """time.sleep(0.20)
                                    GPIO.output(11,GPIO.LOW)
                                    GPIO.output(13,GPIO.LOW)
                                    GPIO.output(15,GPIO.LOW)
                                    GPIO.output(16,GPIO.LOW)
                                    
                                    GPIO.output(18,GPIO.LOW)
                                    GPIO.output(22,GPIO.LOW)
                                    GPIO.output(29,GPIO.LOW)
                                    GPIO.output(31,GPIO.LOW)
                                    time.sleep(0.20)"""
                            elif 380>x>260:
                                    #ser.write('forward')
                                    print 'forward'
                                    GPIO.output(32,GPIO.HIGH)
                                    GPIO.output(33,GPIO.HIGH)
                                    GPIO.output(36,GPIO.HIGH)
                                    GPIO.output(37,GPIO.HIGH)
                                    
                                    GPIO.output(11,GPIO.HIGH)
                                    GPIO.output(13,GPIO.LOW)
                                    GPIO.output(15,GPIO.HIGH)
                                    GPIO.output(16,GPIO.LOW)
                                    
                                    GPIO.output(18,GPIO.HIGH)
                                    GPIO.output(22,GPIO.LOW)
                                    GPIO.output(29,GPIO.HIGH)
                                    GPIO.output(31,GPIO.LOW)
                                    """time.sleep(0.2)
                                    GPIO.output(11,GPIO.LOW)
                                    GPIO.output(13,GPIO.LOW)
                                    GPIO.output(15,GPIO.LOW)
                                    GPIO.output(16,GPIO.LOW)
                                    
                                    GPIO.output(18,GPIO.LOW)
                                    GPIO.output(22,GPIO.LOW)
                                    GPIO.output(29,GPIO.LOW)
                                    GPIO.output(31,GPIO.LOW)
                                    time.sleep(0.2)"""
                                    if radius>75:
                                                    #ser.write('stop')
                                                     print 'stop'
                                                     GPIO.output(32,GPIO.LOW)
                                                     GPIO.output(33,GPIO.LOW)
                                                     GPIO.output(36,GPIO.LOW)
                                                     GPIO.output(37,GPIO.LOW)
                                            
                                                     GPIO.output(11,GPIO.LOW)
                                                     GPIO.output(13,GPIO.LOW)
                                                     GPIO.output(15,GPIO.LOW)
                                                     GPIO.output(16,GPIO.LOW)
                                                     GPIO.output(18,GPIO.LOW)
                                                     GPIO.output(22,GPIO.LOW)
                                                     GPIO.output(29,GPIO.LOW)
                                                     GPIO.output(31,GPIO.LOW)
                                                     time.sleep(0.2)
                                                     print 'servo'

                                                     ser.write('1')
                                                     d = True
                    else :
                                    GPIO.output(32,GPIO.LOW)
                                    GPIO.output(33,GPIO.LOW)
                                    GPIO.output(36,GPIO.LOW)
                                    GPIO.output(37,GPIO.LOW)
                        
                                    GPIO.output(11,GPIO.LOW)
                                    GPIO.output(13,GPIO.LOW)
                                    GPIO.output(15,GPIO.LOW)
                                    GPIO.output(16,GPIO.LOW)
                                    
                                    GPIO.output(18,GPIO.LOW)
                                    GPIO.output(22,GPIO.LOW)
                                    GPIO.output(29,GPIO.LOW)
                                    GPIO.output(31,GPIO.LOW)
                                                 
        elif d == True:
            leave(frame)


	cv2.imshow("Frame", frame)
	if cv2.waitKey(1) & 0xFF ==27:
		break

cv2.destroyAllWindows()
pwm1.stop()
pwm2.stop()
GPIO.cleanup()

