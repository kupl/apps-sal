def day_and_time(mins):
    dow = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return '{} {:02d}:{:02d}'.format(dow[mins // 1440 % 7], mins // 60 % 24, mins % 60)
