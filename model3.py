#TRAFFIC MODELING IN PYTHON 3
#Now assume that traffic light is at an intersction, and with probability p, cars block the intersection
#So with probability p, even though light is green, no cars can pass
#Start with blocking probability at 10%
from trafficLight import TrafficLight
import numpy as np
import matplotlib.pyplot as plt


#Create two AverageWait functions - one for "Clear traffic" i.e. no blocking
#One for blocked traffic

def calculateClearWait(numcars,tl,prob):
  limit = tl.perSecond * tl.greenTime
  if numcars <= limit:
    return numcars*0
  else:
    t = ((numcars-limit)*tl.redTime)
    p = np.random.uniform()
    if p <= prob:
      return t + calculateBlockedWait(numcars-limit,tl,prob)
    else:
      return  t + calculateClearWait(numcars-limit,tl,prob)

#If intersection is blocked, then all cars wait for full 60 seconds before they have a chance of advancing
def calculateBlockedWait(numcars,tl,prob):
  limit = tl.perSecond * tl.greenTime
  #All cars must wait for greenTime + redTime
  t = numcars*(tl.greenTime+tl.redTime)
  p = np.random.uniform()
  if p <= prob:
    return t+calculateBlockedWait(numcars,tl,prob)
  else:
    return t+calculateClearWait(numcars,tl,prob)

#We will compare car arrival rates and blocking probabilities
#Possible values for car arrival rate
rateVals = [x for x in range(2,40,2)]
#Possible blocking probabilities
pVals = [0.0,0.2,0.4,0.6,0.8]

for g in range(20,50,10):
  gyVals = []
  for pr in pVals:
    tl = TrafficLight(g,60-g)

    yVals = []

    for x in rateVals:

      waitTimes = []
      for _ in range(5):
        numCars = np.random.poisson(x)
        if numCars == 0:
          waitTimes.append(0)
        else:
          p = np.random.uniform()
          if p <= pr:
            waitTimes.append(calculateBlockedWait(numCars,tl,pr)/float(numCars))
          else:
            waitTimes.append(calculateClearWait(numCars,tl,pr)/float(numCars))

      yVals.append(sum(waitTimes)/float(len(waitTimes)))

    gyVals.append(yVals)

  i=0
  colors = ['b','r','g','c','m']
  for y, c in zip(gyVals, colors):
    z = np.polyfit(rateVals, y, 1)
    p = np.poly1d(z)
    plt.plot(rateVals,y,'.',color=c)
    plt.plot(rateVals,p(rateVals),'-',color=c,label=("Blocking Probability = %s" % pVals[i]))
    i+=1
  plt.legend(fontsize=9,loc=0)
  plt.xlabel('Car arrival rate per minute', fontsize=12)
  plt.ylabel('Average waiting time (seconds)', fontsize=12)
  plt.suptitle("Average waiting time per car: Green %s seconds" % g)
  # plt.show()
  plt.savefig("images/model_3_%s.png" % g)
  plt.clf()