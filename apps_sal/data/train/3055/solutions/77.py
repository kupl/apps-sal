def sum_str(a, b):
    if (a==None or a=="") and  (b==None or b==""):
        return str(0)
    elif a==None or a=="":
        return b
    elif b==None or b=="":
        return a
    else:
        return str(int(a)+int(b))
