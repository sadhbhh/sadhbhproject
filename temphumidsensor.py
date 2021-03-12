import sys
import Adafruit_DHT as DHT

for x in range(10):
  humid, temp = DHT.read_retry(DHT.DHT11, 4)
  print(temp, humid)
