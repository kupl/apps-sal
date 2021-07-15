def set_alarm(employed, vacation):
    if vacation is True:
        return False
    elif employed == True:
        return True
    elif employed == False:
        return False
