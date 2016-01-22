import numpy as np

class Car(object):

  def __init__(self, start=0, end=60, arrivalTime=0, waitTime=-1):
    self.arrivalTime = np.random.randint(start,end)
    self.waitTime=-1

  def arrivalTime(self):
    return self.arrivalTime

  def arrivalTime(self):
    return self.waitTime

  def __str__(self):
    return "Car arrives at" % (self.arrivalTime)

