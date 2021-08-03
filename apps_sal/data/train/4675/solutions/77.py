def set_alarm(employed, vacation):
    if vacation:
        return False
    if employed and vacation:
        return False
    if employed and not vacation:
        return True
    return False
