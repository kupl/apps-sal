def seven(m):
    num = str(m)
    digits = str(len(num))
    steps = 0
    while int(digits) > 2:
        y = num[-1]
        x = num[:-1]
        num = int(x) - 2*int(y)
        digits = len(str(num))
        steps += 1
        num = str(num)
    return (int(num), steps)
        
        

