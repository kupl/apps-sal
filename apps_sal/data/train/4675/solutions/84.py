def set_alarm(e, v):
    if e == True and v == True:
        return False
    elif e == False and v == True:
        return False
    elif e == False and v == False:
        return False
    elif e == True and v == False:
        return True
