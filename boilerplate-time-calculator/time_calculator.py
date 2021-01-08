def add_time(start, duration, *day):

  hourS = int(start.split(":")[0])
  if "PM" in start:
    hourS += 12
  minS = int(start.split(":")[1].split(" ")[0])
  hourD = int(duration.split(":")[0])
  minD = int(duration.split(":")[1])
  
  hourN = 0
  minN = 0
  
  if minS + minD >= 60:
    minN = minS + minD - 60
    hourN += 1
  else:
    minN = minS + minD

  AmPmVar = ""
  
  days = int((hourN + hourS + hourD)/24)
  hourN = hourN + hourS + hourD
  if hourN % 24 == 0:
      hourN = 24
      AmPmVar = " AM"
  elif hourN % 12 == 0:
      hourN = 12
      AmPmVar = " PM"
  else:
      hourN -= (days * 24) 

  strHourN = []
  strMinN = str(minN)
  if len(strMinN)==1:
      strMinN = "0"+strMinN
  
  addition = []

  if AmPmVar == " AM":
    strHourN = str(hourN - 12) + ":"
    addition = AmPmVar
  elif AmPmVar == " PM":
    strHourN = str(hourN) + ":"
    addition = AmPmVar
  elif hourN > 12:
    strHourN = str(hourN - 12) + ":"
    addition = " PM"
  elif hourN == 12:
    strHourN = str(hourN) + ":"
    addition = " PM"      
  else:
    strHourN = str(hourN) + ":"
    addition = " AM"

  new_time = strHourN + strMinN + addition
  
  if len(day)>0:
      weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
      newDay = weekdays[weekdays.index(day[0].lower()) + days%7].capitalize()
      new_time = new_time + ", " + newDay
  
  if days == 1:
      new_time = new_time + " (next day)"
  if days > 1:
      new_time = new_time + " (" + str(days) + " days later)"

  return new_time