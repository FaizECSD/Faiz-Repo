#define pHpin D34
#define uStoSecondsfactor 1000000ULL
#define sleeptime 60

void setup() {
  pinMode(pHpin, INPUT);
 Serial.begin(9600);
 Serial.print("Ready");

 int pHseries[10];
   for(int i=0;i<10;i++)
   {
    pHseries[i]=analogRead(pHpin);
    delay(10);
   }
   int sumpH=0;
  for(int j=0;j<10;j++)
  {
    sumpH=sumpH+pHseries[j];
  }
float avgpH=sumpH/10;
float pHvolt=avgpH*5.0/1024/6;
float pH= 7.0+((2.5-pHvolt)/0.18);
Serial.print("pH Value:");
Serial.print(pH,2);

esp_sleep_enable_timer_wakeup(uStoSecondsfactor*sleeptime);
esp_deep_sleep_start();


}

void loop() {
}
