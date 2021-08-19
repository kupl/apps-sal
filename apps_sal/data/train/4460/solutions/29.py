def whatday(num):
    day = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    return day[num % 7] if num in range(1, 8) else 'Wrong, please enter a number between 1 and 7'
