def whatday(num):
    days = ('Sun', 'Mon', 'Tues', 'Wednes', 'Thurs', 'Fri', 'Satur')
    return days[num-1] + 'day' if 0 < num < 8 else 'Wrong, please enter a number between 1 and 7' 
