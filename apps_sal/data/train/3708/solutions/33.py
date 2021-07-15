def hex_to_dec(s):
    t = 0
    x = len(s) -1
    for i in s:
        
        if i=="a":
            t+= (10*(16**x))
        elif i=="b":
            t+= (11*(16**x))
        elif i=="c":
            t+= (12*(16**x))
        elif i=="d":
            t+= (13*(16**x))
        elif i=="e":
            t+= (14*(16**x))
        elif i=="f":
            t+= (15*(16**x))
        else:
            t+= (int(i)*(16**x))

        x-=1

    print(t)
    return t 
