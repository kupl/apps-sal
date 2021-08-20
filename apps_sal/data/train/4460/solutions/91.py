def whatday(num):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return days[num - 1] if num <= len(days) and num != 0 else 'Wrong, please enter a number between 1 and 7'
