def closest(lst):
    mn = min(lst, key=abs)
    return mn if -mn not in lst or mn == 0 else None
