def set_alarm(employed, vacation):
    if employed is True and vacation is True:
        return False
    if employed is False and vacation is True:
        return False
    if employed is True and vacation is False:
        return True
    if employed is False and vacation is False:
        return False

