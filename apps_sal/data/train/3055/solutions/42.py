def sum_str(a, b):
    print((a,b))
    if a==b=="":
        return "0"
    if a==None or a=="":
        return b
    if b==None or b=="":
        return a
    
    return str(int(a)+int(b))

