class TrafficLight(object):

  def __init__(self, greenTime, redTime, perSecond=0.1, totalTime=60, state=''):
    self.greenTime = greenTime
    self.redTime = redTime
    self.totalTime = greenTime+redTime
    self.state = 'Green'
    self.perSecond = perSecond

  def greenTime(self):
    return self.greenTime

  def redTime(self):
    return self.redTime

  def totalTime(self):
    return self.totalTime

  def totalTime(self):
    return self.perSecond

  def updateLight(self,greenTime=None,redTime=None,perSecond=None):
    if greenTime:
      self.greenTime = greenTime
    if redTime:
      self.redTime = redTime
    if perSecond:
      self.perSecond = perSecond

  def changeState(self):
    if self.state == 'Red':
      self.state = 'Green'
    else:
      self.state = 'Red'

  def __str__(self):
    return "Green time is %s, Red time is %s, Pass rate is %s" % (self.greenTime, self.redTime, self.perSecond)

  # def operateLight():
