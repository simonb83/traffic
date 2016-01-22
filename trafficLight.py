class TrafficLight(object):

  def __init__(self, greenTime, redTime, totalTime=0, state=''):
    self.greenTime = greenTime
    self.redTime = redTime
    self.totalTime = greenTime+redTime
    self.state = 'Green'

  def greenTime(self):
    return self.greenTime

  def redTime(self):
    return self.redTime

  def totalTime(self):
    return self.totalTime

  def changeState(self):
    if self.state == 'Red':
      self.state = 'Green'
    else:
      self.state = 'Red'

  def __str__(self):
    return "Light is %s" % (self.state)

  # def operateLight():
