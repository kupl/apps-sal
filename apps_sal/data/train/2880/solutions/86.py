def seven(m):
    
    num = str(m)
    steps = 0
    
    while len(num) >2:
        x = num[:-1]
        y = num[-1]
        num = str(int(x) - 2*int(y))
        steps += 1

    return (int(num),steps)

