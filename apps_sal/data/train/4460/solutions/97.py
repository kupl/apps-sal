def whatday(num):
  # Put your code here
  weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']  
  if num in range(1,8):
      return weekdays[num - 1]
  return 'Wrong, please enter a number between 1 and 7'
