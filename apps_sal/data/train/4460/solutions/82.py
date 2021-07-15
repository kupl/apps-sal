def whatday(num):
    if num == 1:
        result = "Sunday"
    elif num == 2:
        result = "Monday"
    elif num == 3:
        result = "Tuesday"
    elif num == 4:
        result = "Wednesday"
    elif num == 5:
        result = "Thursday"
    elif num == 6:
        result = "Friday"
    elif num == 7:
        result = "Saturday"
    else:
        result = "Wrong, please enter a number between 1 and 7"
    return result
