def set_alarm(e, v):
    if e==True and v==True:
        return False
    elif e==True and v==False:
        return True
    elif e==False and v==True:
        return False
    else:
        return False
