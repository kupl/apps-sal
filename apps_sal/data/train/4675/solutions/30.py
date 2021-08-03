def set_alarm(e, v):
    return False if e and v or e == False and v == True or [e, v] == [False, False] else True
