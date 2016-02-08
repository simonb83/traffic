#TRAFFIC MODELING IN PYTHON 2
#Multiple cars arrive in 60-second interval with rate R
from trafficLight import TrafficLight
import numpy as np
import matplotlib.pyplot as plt


#Numcar is number of cars that have arrived. Limit is based on traffic flow per second & number of seconds traffic light is green
#If less cars arrive than the limit, then all cars have 0 waiting time
#If more cars arrive than the limit, then the cars > limit must wait for red time + average waiting time for thos cars when light changes
def calculateAverageWait(numcars,limit,redTime):
  if numcars <= limit:
    return numcars*0
  else:
    return ((numcars-limit)*redTime)+ calculateAverageWait(numcars-limit,limit,redTime)

#3 types of variables: Green Time, Car arrival rate, perSecond rate for cars

#Possible values for car arrival rate
rateVals = [x for x in range(2,40,2)]
#Possible values for cars that can pass traffic light per second
passVals = [0.1,0.2,0.3,0.4,0.5]
#Possible values for green % of traffic light time
grVals = [0.2,0.3,0.4,0.5,0.6,0.7]


#1 Different arrival rates with different green light % times
gyVals = []

for g in grVals:
  tl = TrafficLight(g*60,(1-g)*60)
  limit = tl.perSecond * tl.greenTime

  yVals = []

  for x in rateVals:
    waitTimes = []
    for _ in range(20):
      numCars = np.random.poisson(x)
      if numCars == 0:
        waitTimes.append(0)
      else:
        waitTimes.append(calculateAverageWait(numCars,limit,tl.redTime)/float(numCars))

    yVals.append(sum(waitTimes)/float(len(waitTimes)))

  gyVals.append(yVals)


i=0
colors = ['b','r','g','c','m','k']
for y, c in zip(gyVals, colors):
  z = np.polyfit(rateVals, y, 1)
  p = np.poly1d(z)
  plt.plot(rateVals,y,'.',color=c)
  plt.plot(rateVals,p(rateVals),'-',color=c,label=("Green Proportion = %s%%" % int(grVals[i]*100)))
  i+=1
plt.legend(fontsize=9, loc=0)
plt.xlabel('Car arrival rate per minute', fontsize=12)
plt.ylabel('Average waiting time (seconds)', fontsize=12)
plt.suptitle("Varying Car Arrival Rate & Green Time %")
plt.xlim([0,40])
# plt.show()
plt.savefig("images/model_2A.png")
plt.clf()


#2 Different arrival rates with different rates that cars can pass (traffic flow)
gyVals = []

for g in passVals:
  tl = TrafficLight(30,30,g)
  limit = tl.perSecond * tl.greenTime

  yVals = []

  for x in rateVals:
    waitTimes = []
    for _ in range(20):
      numCars = np.random.poisson(x)
      if numCars == 0:
        waitTimes.append(0)
      else:
        waitTimes.append(calculateAverageWait(numCars,limit,tl.redTime)/float(numCars))

    yVals.append(sum(waitTimes)/float(len(waitTimes)))

  gyVals.append(yVals)


i=0
colors = ['b','r','g','c','m','k']
for y, c in zip(gyVals, colors):
  z = np.polyfit(rateVals, y, 1)
  p = np.poly1d(z)
  plt.plot(rateVals,y,'.',color=c)
  plt.plot(rateVals,p(rateVals),'-',color=c,label=("Traffic Flow per Second = %s" % passVals[i]))
  i+=1
plt.legend(fontsize=9, loc=0)
plt.xlabel('Car arrival rate per minute', fontsize=12)
plt.ylabel('Average waiting time (seconds)', fontsize=12)
plt.suptitle("Varying Car Arrival Rate & Car Flow")
plt.xlim([0,40])
# plt.show()
plt.savefig("images/model_2B.png")