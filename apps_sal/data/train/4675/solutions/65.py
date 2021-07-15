def set_alarm(x, y):
    if x == True and y == True:
        return False
    elif x == False and y == True:
        return False
    elif x == False and y == False:
        return False
    else:
        return True
