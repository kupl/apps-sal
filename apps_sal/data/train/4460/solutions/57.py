def whatday(num):
    array = [0, 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return 'Wrong, please enter a number between 1 and 7' if num == 0 or num > 7 else array[num]
