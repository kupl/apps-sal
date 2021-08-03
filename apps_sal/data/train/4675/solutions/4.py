set_alarm = lambda *a: a == (1, 0)
set_alarm = lambda *a: a == (True, False)  # [1]
def set_alarm(employed, vacation): return (employed, vacation) == (True, False)  # [2]
def set_alarm(employed, vacation): return (employed == True) and (vacation == False)
def set_alarm(employed, vacation): return employed and not vacation

# The most voted best practice solution:


def set_alarm(employed, vacation):    # [3]
    return employed and not vacation  #
