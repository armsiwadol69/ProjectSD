#include <LiquidCrystal_PCF8574.h>
#include <Wire.h>
#include "DHT.h"
#define DHTPIN 13     // what pin we're connected to
// Uncomment whatever type you're using!
#define DHTTYPE DHT11   // DHT 11 
//#define DHTTYPE DHT22   // DHT 22  (AM2302)
//#define DHTTYPE DHT21   // DHT 21 (AM2301)
int led = 12;
int ledpower = 11;
// Initialize DHT sensor for normal 16mhz Arduino
DHT dht(DHTPIN, DHTTYPE);
LiquidCrystal_PCF8574 lcd(0x27);
void setup() {
  digitalWrite(ledpower, HIGH);
  Wire.begin();
  Wire.beginTransmission(0x27);
  Serial.begin(9600); 
  dht.begin();
  lcd.begin(16, 2);
//Serial.println("DHTxx test!");
  lcd.clear();
  lcd.setBacklight(255);
  lcd.print("Now Starting");
  lcd.setCursor(0, 1); 
  lcd.print("By SiWADOL M.");
  delay(1000);
  lcd.clear();
  lcd.setBacklight(255);
  lcd.print("YOUR MOM GAY");
  lcd.setCursor(0, 1); 
  //delay(1000);
  lcd.print("Mizuki is CUTE!");
  delay(1000);
  lcd.clear();
  lcd.print("LOADING...");
  lcd.setCursor(0, 1); 
  lcd.print("1st Read'n 5 s.");
  pinMode(led, OUTPUT); 
}

void loop() {
  // Wait a few seconds between measurements.
  lcd.clear();
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit
  float f = dht.readTemperature(true);
  
  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    digitalWrite(ledpower, HIGH);
    digitalWrite(led, HIGH);
    return;
  }
  // Compute heat index
  // Must send in temp in Fahrenheit!
  float hi = dht.computeHeatIndex(f, h);
  //Serial.print("Humidity: "); 
  Serial.print(h);  //HUMI
  Serial.print(" ");
  //Serial.print(" %\t");
  //Serial.print("Temperature: "); 
  Serial.print(t);  //TEMP
  Serial.println();
  //Serial.print(" *C ");
  //Serial.print(f);
  //Serial.print(" *F\t");
  //Serial.print("Heat index: ");
  //Serial.print(hi);
  //Serial.println(" *F");
  lcd.print("Humi : "); //LCD
  lcd.print(h);
  lcd.print("%");
  lcd.print("Temp : "); //LCD
  lcd.print(f);
  digitalWrite(led, HIGH);
  delay(500);
  digitalWrite(led, LOW);
  delay(4000);
  }
