def whatday(num):
    arr = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday',
           6: 'Friday', 7: 'Saturday'}

    if num <= 7 and num > 0:
        return arr[num]
    else:
        return 'Wrong, please enter a number between 1 and 7'
