def whatday(num):
  days = {1: "Sunday",2: "Monday",3: "Tuesday",4: "Wednesday",5: "Thursday",6: "Friday",7: "Saturday"}
  if num not in days:
      return "Wrong, please enter a number between 1 and 7"
  return days[num]
  
  
  

