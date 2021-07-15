def whatday(num):
  days={1:'Sunday', 2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday',7:'Saturday'}
  WRONG_VALUE="Wrong, please enter a number between 1 and 7"
  return days.get(num,WRONG_VALUE)
