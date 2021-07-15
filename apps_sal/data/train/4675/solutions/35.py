def set_alarm(employed, vacation):
    if employed == True:
        if vacation == True:
            return False
        if vacation == False:
            return True
    if employed == False:
        return False
