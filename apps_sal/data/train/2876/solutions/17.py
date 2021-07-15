def check(a, x): 
    if len(a) == 0: return False
    item = a.pop()
    if item == x: return True
    else: return check(a, x)
