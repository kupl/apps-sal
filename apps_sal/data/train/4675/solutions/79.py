def set_alarm(employed, vacation):
    if employed == True and vacation == True:
        return False
    else:
        return False if employed == False else True
