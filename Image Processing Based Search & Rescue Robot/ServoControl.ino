#include <Servo.h>  /* Servo kutuphanesi projeye dahil edildi */
Servo servoNesnesi; /* servo motor nesnesi yaratildi */
Servo servoNesnesi1;

void setup()
{
  servoNesnesi.attach(9);  /* Servo motor 9 numarali pine baglandi */
  Serial.begin(9600);
}

void loop()
{
  while (Serial.available()) 
  {
  

 
    char d = Serial.read(); 
    Serial.print(d);
    
    
    if (d == '1')
    {
      servoNesnesi.write(65);  
      delay(2000);
    }

    if (d == '2')
    {
      servoNesnesi.write(150);
  
      delay(2000);
      
    }
    
  }
}






