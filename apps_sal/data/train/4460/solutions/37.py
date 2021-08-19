def whatday(num):
    d = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
    return d.get(num) if num > 0 and num < 8 else 'Wrong, please enter a number between 1 and 7'
