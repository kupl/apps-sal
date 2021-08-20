def whatday(num):
    arr = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if num > 0 and num < 8:
        return str(arr[num - 1])
    else:
        return 'Wrong, please enter a number between 1 and 7'
