for _ in range(int(input())):
    q = input()
    x = 0
    o = 0
    y = '=' + q
    z = -1
    c = -1
    for i in range(1, len(y)):
        if(y[i] == '>') and (y[i - 1] == '=' or y[i - 1] == '>'):
            x += 1
        elif(y[i] == '<') and (y[i - 1] == '=' or y[i - 1] == '<'):
            o += 1
        elif(y[i] == '='):
            continue
        else:
            if(z < o):
                z = o
            if(c < x):
                c = x
            if(y[i] == '>'):
                x = 1
                o = 0
            if(y[i] == '<'):
                o = 1
                x = 0
    if(z < o):
        z = o
    if(c < x):
        c = x
    print(max(z, c, 0) + 1)
