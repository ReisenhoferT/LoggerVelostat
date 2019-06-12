/***************************************************************************
  This is a library for the BME280 humidity, temperature & pressure sensor
  Designed specifically to work with the BME280 Breakout board
  ----> http://www.adafruit.com/products/2650
  This sketch only supports the I2C bus for connection.
 ***************************************************************************/

#include <Wire.h>
#include "cactus_io_BME280_I2C.h"

// Create the BME280 object
//BME280_I2C bme;              // I2C using default 0x77 
BME280_I2C bme(0x76);  // I2C using address 0x76
//int nb_seconds = 1800;
int nb_seconds_int = 6;
int nb_seconds = 30;
int time_stp = 0;
int sensor_output =0;
int VRef = 5;
int max_scale = 1023;
int R_pont = 560;

float int_to_volt(const int & val) {
  return float(val * VRef) / float (max_scale);
}

float R1(const float & U, const float & U2, const float & R2) {
  return (R2 * (U - U2)) / (U2);
}


void setup() {
  Serial.begin(9600);
  bme.begin();
  bme.setTempCal(-1);
  delay(3000);
  
}

void loop() {
  int count = 0;
  float mean_R1 = 0;
  
  for (int j=0; j< nb_seconds_int; j++) {
    
  
    sensor_output = analogRead(A0);
    float voltage = int_to_volt(sensor_output);
    float Val_R1 = R1(float(VRef), voltage, float(R_pont));
    mean_R1 = (float(count) * mean_R1 + Val_R1) / (float(count+1));
    count ++;
    delay(1000);  
  }
    bme.readSensor();
    Serial.print(bme.getPressure_MB()); Serial.print(",");    // Pressure in millibars
    Serial.print(bme.getHumidity()); Serial.print(",");
    Serial.print(bme.getTemperature_C()); Serial.print(",");
    Serial.print(mean_R1); Serial.println("\n");


    // add a 2 second delay to slow down the output
    // TODO: Attention delay(long) maximum tempo de 65 sec écrire une fonction
    // écrire une fonction pour avoir des second et des minutes.
    for(int i=0; i<nb_seconds; i ++) 
      delay(1000);
}
