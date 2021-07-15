set_alarm=lambda *a:a==(1,0)
set_alarm = lambda *a: a == (True, False) # [1]
set_alarm = lambda employed, vacation: (employed, vacation) == (True, False) # [2]
set_alarm = lambda employed, vacation: (employed == True) and (vacation == False)
set_alarm = lambda employed, vacation: employed and not vacation

# The most voted best practice solution:

def set_alarm(employed, vacation):    # [3]
    return employed and not vacation  #

