#TRAFFIC MODELING IN PYTHON 4 Part I
#Minute by minute simulation for traffic light at intersection
#Some important assumptions:
#Rate at which traffic can pass green light decreases as function of number of cars waiting
#Arrival rate of cars varies during time period
#Probability that other cars block intersection also varies during time period, roughly in-line with arrival rate of cars
#If cars block intersection, the time for which they block the intersection can vary

#Key variables:
#Proportion of time the Traffic Light is green or red (per minute)
#Car arrival rate
#Rate at which cars can pass the light per second
#Probability that the intersection is blocked when the Traffic Light is Green
#Time for which the intersection is blocked when the Traffic Light is Green

#Rough pseudo-code
#Number of cars arrive and join the queue of cars
#For that time period, calculate how many cars pass
#Calculate new queue
#Calculate average waiting time for that period

from trafficLight import TrafficLight
from car import Car
import numpy as np
import matplotlib.pyplot as plt
import statistics

#Green proportion:
grProp = 0.5
grTime = grProp*60
rdTime = 60-grTime

#Car arrival rates for low, medium and high-peak times
arriveRates = {'L':8, 'M':12, 'H':20}
# arriveRates = {'L':10, 'M':14, 'H':25}

#perSecond Rate for low, medium and high-peak times
passRates = {'L':1, 'M':0.9*1, 'H':0.9*0.8*1}

#Probability that intersection is blocked in low, medium and high-peak times
blockingProb = {'L':0.05, 'M':0.2, 'H':0.45}

#% of time for which intersection is blocked in low, medium and high-peak times
bloockingTime = {'L':0.05, 'M':0.2, 'H':0.5}

#Calculate the time it takes to pass during the interval for the cars that manage to pass the light
def calcPassTime(number, normalGreenTime, actualGreenTime):
  allWaitFor = normalGreenTime - actualGreenTime
  if number > 0:
    timeperCar = actualGreenTime/float(number)
  else:
    timeperCar = 0
  times = []
  for i in range(1,number+1,1):
    times.append(timeperCar*i+allWaitFor)
  return times

def runTraffic(queue, passedCars, tl, trafficType):
  p = np.random.uniform()
  if p < blockingProb[trafficType]:
    greenTime = (tl.greenTime - bloockingTime[trafficType]*tl.greenTime)
  else:
    greenTime = tl.greenTime

  passableCars = int(greenTime*tl.perSecond)
  
  if len(queue) <= passableCars:
    top = len(queue)
  else:
    top = passableCars

  totalTime = 0
  times = calcPassTime(top,tl.greenTime,greenTime)
  for j in range(top):
    car = queue[j]
    car.updateWaitTime(times[j])
    totalTime += car.waitTime
    passedCars.append(car)

  avg = 0
  if top > 0:
    avg = totalTime/float(top)

  for j in range(top,len(queue),1):
    car = queue[j]
    car.updateWaitTime(tl.totalTime)

  del queue[0:passableCars]
  return queue, passedCars, top, avg

#Number of cars still waiting in queue
yValsA = []
#Number of cars passing per minute
yValsB = []
#Average wait time of cars passing per minute
yValsC = []
#Array of car wait times for each passing car in that interval
yValsD = []

for z in range(1000):

  tl = TrafficLight(grTime,rdTime,passRates['L'])
  carQueue = []
  passedCars = []

  numWaitingCars = []
  numPassedCars = []
  avgWaitTime = []

  for i in range(5):
    for _ in range(np.random.poisson(arriveRates['L'])):
      carQueue.append(Car())

    carQueue, passedCars, numCars, avgTime = runTraffic(carQueue,passedCars,tl,'L')
    numWaitingCars.append(len(carQueue))
    numPassedCars.append(numCars)
    avgWaitTime.append(avgTime)

  for i in range(5,20,1):
    tl.updateLight(40,20,passRates['H'])
    for _ in range(np.random.poisson(arriveRates['H'])):
      carQueue.append(Car())

    carQueue, passedCars, numCars, avgTime = runTraffic(carQueue,passedCars,tl,'H')
    numWaitingCars.append(len(carQueue))
    numPassedCars.append(numCars)
    avgWaitTime.append(avgTime)

  for i in range(20,40,1):
    tl.updateLight(30,30,passRates['M'])
    for _ in range(np.random.poisson(arriveRates['M'])):
      carQueue.append(Car())

    carQueue, passedCars, numCars, avgTime = runTraffic(carQueue,passedCars,tl,'M')
    numWaitingCars.append(len(carQueue))
    numPassedCars.append(numCars)
    avgWaitTime.append(avgTime)

  for i in range(40,55,1):
    tl.updateLight(40,20,passRates['H'])
    for _ in range(np.random.poisson(arriveRates['H'])):
      carQueue.append(Car())

    carQueue, passedCars, numCars, avgTime = runTraffic(carQueue,passedCars,tl,'H')
    numWaitingCars.append(len(carQueue))
    numPassedCars.append(numCars)
    avgWaitTime.append(avgTime)

  for i in range(55,60,1):
    tl.updateLight(30,30,passRates['L'])
    for _ in range(np.random.poisson(arriveRates['L'])):
      carQueue.append(Car())

    carQueue, passedCars, numCars, avgTime = runTraffic(carQueue,passedCars,tl,'L')
    numWaitingCars.append(len(carQueue))
    numPassedCars.append(numCars)
    avgWaitTime.append(avgTime)

  yValsA.append(numWaitingCars)
  yValsB.append(numPassedCars)
  yValsC.append(avgWaitTime)
  yValsD.append([car.waitTime for car in passedCars])

x = [i+1 for i in range(60)]

plt.plot(x,[sum(e)/len(e) for e in zip(*yValsA)],'-o',label="Size of queue")
plt.plot(x,[sum(e)/len(e) for e in zip(*yValsB)],'-o',label="Number of passed cars")
plt.legend(fontsize=9,loc=0)
plt.xlabel('Minute', fontsize=12)
plt.ylabel('Number of Cars', fontsize=12)
plt.suptitle("Number of waiting & passing cars per interval")
plt.savefig("images/model4_numCars.png")

plt.clf()

plt.plot(x,[sum(e)/len(e) for e in zip(*yValsC)],'-o',label="Average of avg. waiting time over 1000 tests")
plt.plot(x,[max(e) for e in zip(*yValsC)],'-o',label="Max of avg. waiting time over 1000 tests")
plt.plot(x,[statistics.median(e) for e in zip(*yValsC)],'-o',label="Median of avg. waiting time over 1000 tests")
plt.legend(fontsize=9,loc=0)
plt.xlabel('Minute', fontsize=12)
plt.ylabel('Number of seconds', fontsize=12)
plt.suptitle("Average wait time per interval")
plt.savefig("images/model4_avgTime.png")

plt.clf()

allWaitTimes = []
for r in yValsD:
  for t in r:
    allWaitTimes.append(t)

plt.hist(allWaitTimes,bins=40,normed=True,alpha=0.5,color='g')
plt.suptitle("Distribution of car wait times")
plt.xlabel('Car Wait Time (secs)', fontsize=12)
plt.ylabel('%', fontsize=12)
plt.savefig("images/model4_hist.png")

plt.clf()

plt.hist(allWaitTimes,bins=40,normed=True,alpha=0.5,color='r',cumulative=True)
plt.suptitle("Distribution of car wait times")
plt.xlabel('Car Wait Time (secs)', fontsize=12)
plt.ylabel('Cumulative %', fontsize=12)
plt.savefig("images/model4_hist_cum.png")
