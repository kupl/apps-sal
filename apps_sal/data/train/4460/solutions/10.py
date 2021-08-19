def whatday(num):
    lst = ['Wrong, please enter a number between 1 and 7', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return lst[num] if num > 0 and num < 8 else lst[0]
