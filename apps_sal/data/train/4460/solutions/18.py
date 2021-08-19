def whatday(numb):
    if numb not in range(1, 8):
        return 'Wrong, please enter a number between 1 and 7'
    elif numb == 1:
        return 'Sunday'
    elif numb == 2:
        return 'Monday'
    elif numb == 3:
        return 'Tuesday'
    elif numb == 4:
        return 'Wednesday'
    elif numb == 5:
        return 'Thursday'
    elif numb == 6:
        return 'Friday'
    elif numb == 7:
        return 'Saturday'
