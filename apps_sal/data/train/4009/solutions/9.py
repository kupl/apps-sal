import math


def digits_average(num):
    a = str(num)
    b = []
    a = [n for n in a]
    for i in a:
        b.append(int(i))
    if(len(b) == 1):
        return b[0]
    while(len(a) > 1):
        c = 0
        while(c <= len(b) - 2):
            d = b[c] + b[c + 1]
            d = math.ceil(d / 2)
            b[c] = d
            c += 1
        del(b[len(b) - 1])
        if(len(b) == 1):
            return b[0]
