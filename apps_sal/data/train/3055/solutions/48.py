from functools import reduce
def sum_str(a, b):
    if a=="" and b=="":
        return "0"
    elif a=="":
        return str(b)
    elif b=="":
        return str(a) 
    else:
        return str(int(a)+int(b))

