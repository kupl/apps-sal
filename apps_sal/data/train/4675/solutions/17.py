def set_alarm(employed, vacation):
    while employed == True and vacation == True:
        return False
    while employed == False and vacation == True:
        return False
    while employed == True and vacation == False:
        return True
    while employed == False and vacation == False:
        return False


set_alarm(True, True)
