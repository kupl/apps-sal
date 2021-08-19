def whatday(num):
    if 1 <= num <= 7:
        if num == 1:
            return 'Sunday'
        elif num == 2:
            return 'Monday'
        elif num == 3:
            return 'Tuesday'
        elif num == 4:
            return 'Wednesday'
        elif num == 5:
            return 'Thursday'
        elif num == 6:
            return 'Friday'
        else:
            return 'Saturday'
    else:
        return 'Wrong, please enter a number between 1 and 7'
