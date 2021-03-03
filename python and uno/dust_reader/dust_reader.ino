#include "PMS.h"

PMS pms(Serial);
PMS::DATA data;


void setup()

{
  delay(5000);
  Serial.begin(9600);
}

void loop()
{
  if (pms.read(data))
  {
    //Serial.print("PM 1.0 (ug/m3): ");
    Serial.print(data.PM_AE_UG_1_0);
    Serial.print(" ");
    //Serial.print("PM 2.5 (ug/m3): ");
    Serial.print(data.PM_AE_UG_2_5);
    Serial.print(" ");
    //Serial.print("PM 10.0 (ug/m3): ");
    Serial.print(data.PM_AE_UG_10_0);

    Serial.println();
    
  }
  
  // Do other stuff...
}
