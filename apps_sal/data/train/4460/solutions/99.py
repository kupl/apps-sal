def whatday(num):
    print(num)
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return days.pop(num - 1) if num <= len(days) and num > 0 else 'Wrong, please enter a number between 1 and 7'
