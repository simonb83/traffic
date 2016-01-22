from trafficLight import TrafficLight
from car import Car
import numpy as np

def calculateWaitTime(tl,car):
  if car.arrivalTime <= tl.greenTime:
    return 0
  else:
    return tl.totalTime - car.arrivalTime

globalAverages = []

for j in range(10,60,10):
  tl = TrafficLight(j,60-j)
  
  averages = []
  for x in range(20):
    
    waitTimes = []
    for _ in range(20):
      car = Car(0,60)
      w = calculateWaitTime(tl,car)
      waitTimes.append(w)
      
    averages.append(sum(waitTimes)/float(len(waitTimes)))

  globalAverages.append([j,sum(averages)/float(len(averages))])

for entry in globalAverages:
  print "When Traffic Light is Green for %s seconds, average wait time is %s" % (entry[0],entry[1])
