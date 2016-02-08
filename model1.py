#TRAFFIC MODELING IN PYTHON 1
#Simplest model where we look at 1 minute intervals where the light is Green for x seconds and Red for 60-x seconds
#We look at single cars arriving at the light during 1 minute intervals and calculate their average waiting times

from trafficLight import TrafficLight
import random
import numpy as np
import matplotlib.pyplot as plt

#Assume the traffic light starts out green; if the car arrives while the light is still green, wait time is 0
#Otherwise car must wait for remaing red light time before it can pass
def calculateWaitTime(tl,car):
  if car <= tl.greenTime:
    return 0
  else:
    return tl.totalTime - car

globalAverages = []

for j in range(1,100,1):
  #Look over range of green light proportions
  gT = j*60/100
  tl = TrafficLight(gT,60-gT)
  
  averages = []
  for x in range(20):
    
    waitTimes = []
    for _ in range(20):
      #Car arrival time is uniform on 0-60
      car = random.randint(0,60)
      w = calculateWaitTime(tl,car)
      waitTimes.append(w)
      
    averages.append(sum(waitTimes)/float(len(waitTimes)))

  globalAverages.append(sum(averages)/float(len(averages)))

x = [y for y in range(1,100,1)]

plt.scatter(x,globalAverages)
plt.suptitle("Average waiting time for single car")
plt.xlabel("% of period traffic light is green", fontsize=12)
plt.ylabel('Average waiting time (seconds)', fontsize=12)
plt.xlim([0,100])
plt.savefig("images/model_1.png")