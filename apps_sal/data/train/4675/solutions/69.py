def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    elif (employed == True and vacation == True) or (employed == False and vacation == True) or (employed == False and vacation == False):
        return False

