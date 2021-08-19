def set_alarm(employed, vacation):
    if employed:
        if vacation:
            return False
        return True
    return False
