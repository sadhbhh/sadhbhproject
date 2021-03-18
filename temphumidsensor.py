import sys
import Adafruit_DHT as DHT

tempss=[]
humidss=[]

for x in range(10):
  humid, temp = DHT.read_retry(DHT.DHT11, 4)
  print(temp, humid)
  tempss.append(temp)
  humidss.append(humid)
  
def Average(tempss):
   return sum(tempss) // 10
  
def Average(humidss):
   return sum(humidss) // 10

tempavg = Average(tempss)
print("The temperature is", tempavg, "degrees Celsius")

humidavg = Average(humidss)
print("The humidity is", humidavg)

