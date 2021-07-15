def set_alarm(employed, vacation):
    if vacation is True:
        return False
    else:
        if employed is True:
            return True
    return False
