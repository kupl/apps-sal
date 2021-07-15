def whatday(num=''):
    if num > 7 or num == 0:
        return 'Wrong, please enter a number between 1 and 7'
    else:
           return {1 : 'Sunday',
                   2 : 'Monday',
                   3 : 'Tuesday',
                   4 : 'Wednesday',
                   5 : 'Thursday',
                   6 : 'Friday',
                   7 : 'Saturday'}.get(num)

