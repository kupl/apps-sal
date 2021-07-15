def solve(d):
    if (d%4) != 2:
        for i in range(1,(d//2)+1):
            if (d+(i*i))**.5 % 1 == 0:
                return i*i
    return -1
