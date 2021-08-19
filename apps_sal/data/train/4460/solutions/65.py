def whatday(num):
    return {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}[num] if num < 8 and num > 0 else 'Wrong, please enter a number between 1 and 7'
