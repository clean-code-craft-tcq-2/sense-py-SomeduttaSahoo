import math
def calculateStats(numbers):
    computedStats = {}
    if numbers == []:
        computedStats["min"] = float('nan')
        computedStats["max"] = float('nan')
        computedStats["avg"] = float('nan')
     else:
        computedStats["min"] = min(numbers)
        computedStats["max"] = max(numbers)
        computedStats["avg"] = sum(numbers)/len(numbers)
      return computedStats

class EmailAlert:
    def __init__(self):
        self.emailSent = False
 class LEDAlert:
    def __init__(self):
        self.ledGlows = False
 class StatsAlerter:
    def __init__(self, maxThreshold, alert):
        self.maxThreshold = maxThreshold
        self.alert = alert
    def checkAndAlert(self, values):
        for i in values:
            if i >=  self.maxThreshold:
                self.alert[0].emailSent = True
                self.alert[1].ledGlows = True
                break
emailAlert = EmailAlert()
ledAlert   = LEDAlert()
maxThreshold = 10.5
statsAlerter = StatsAlerter(maxThreshold, [emailAlert, ledAlert])
statsAlerter.checkAndAlert([22.6, 12.5, 3.7])
print(ledAlert.ledGlows)
print(emailAlert.emailSent)
       
        
    
  
 
