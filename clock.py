
class Clock(object):

  def __init__(self,hour=0,minute=0):
    self.hour = hour
    self.minute = minute

  def reset(self):
    self.hour = 0
    self.minute = 0

  @property
  def minute(self):
    return self._minute
 
  @minute.setter
  def minute(self,minute):
    self._minute = minute % 60

  @property
  def hour(self):
    return self._hour
 
  @hour.setter
  def hour(self,hour):
    self._hour = hour % 24

  def incrementMinute(self):
    currMin = self.minute
    self.minute += 1
    if currMin == 59:
      self.hour += 1

  def time(self):
    return self.hour, self.minute

  def __str__(self):
    return "{hr:02}:{min:02}".format(hr=self.hour, min=self.minute)

class ImprovedClock(Clock):

  def __init__(self,hour=0,minute=0,second=0):
    Clock.__init__(self,hour,minute)
    self.second = second

  @property
  def second(self):
      return self._second

  @second.setter
  def second(self,second):
    self._second = second % 60 

  def reset(self):
    self.hour = 0
    self.minute = 0
    self.second = 0

  def incrementSecond(self):
    currSec = self.second
    self.second += 1
    if currSec == 59:
      self.incrementMinute()

  def time(self):
    return self.hour, self.minute, self.second

  def __str__(self):
    return "{hr:02}:{min:02}:{sec:02}".format(hr=self.hour, min=self.minute, sec=self.second)

