def whatday(num):
    if num <= 0 or num > 7:
        return "Wrong, please enter a number between 1 and 7"
    else:
        if num == 1:
            return "Sunday"
        elif num == 2:
            return "Monday"
        elif num == 3:
            return "Tuesday"
        elif num == 4:
            return "Wednesday"
        elif num == 5:
            return "Thursday"
        elif num == 6:
            return "Friday"
        else:
            return "Saturday"
