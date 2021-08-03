def set_alarm(employed, vacation):
    if employed == False:
        if vacation == True:
            return False
        if vacation == False:
            return False
    else:
        return bool(vacation) ^ bool(employed)
