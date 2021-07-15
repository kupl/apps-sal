def set_alarm(employed, vacation):
    if bool(employed) and not bool(vacation):
        return True
    else:
        return False
