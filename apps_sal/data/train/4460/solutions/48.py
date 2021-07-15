def whatday(num):
    weekdays = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
    wrong = 'Wrong, please enter a number between 1 and 7'
    return weekdays.get(num, wrong)
