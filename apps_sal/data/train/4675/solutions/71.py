def set_alarm(employed, vacation):
    return (False, True)[employed and (not vacation)]
