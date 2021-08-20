def set_alarm(employed, vacation):
    if employed == True & vacation == True:
        return False
    if employed == False & vacation == False:
        return False
    if employed == False & vacation == True:
        return False
    else:
        return True
