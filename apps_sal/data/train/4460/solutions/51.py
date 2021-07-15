def whatday(num):
    msg = ['Wrong, please enter a number between 1 and 7', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return msg[num] if num in range(1, 8) else msg[0]
