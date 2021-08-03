def set_alarm(employed, vacation):
    if employed == True:
        if vacation == True:
            return False
        else:
            return True
    elif employed == False:
        if vacation == True:
            return False
        else:
            return False
