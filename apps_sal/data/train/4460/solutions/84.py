DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def whatday(num):
    return DAYS[num - 1] if 1 <= num <= 7 else 'Wrong, please enter a number between 1 and 7'
