def set_alarm(employed, vacation):
    if employed:
        if vacation == False:
            return True
        if vacation:
            return False
    else:
        return False
