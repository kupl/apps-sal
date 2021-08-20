set_alarm = lambda *a: a == (1, 0)
set_alarm = lambda *a: a == (True, False)


def set_alarm(employed, vacation):
    return (employed, vacation) == (True, False)


def set_alarm(employed, vacation):
    return employed == True and vacation == False


def set_alarm(employed, vacation):
    return employed and (not vacation)


def set_alarm(employed, vacation):
    return employed and (not vacation)
