def min(a, b):
    if(a < b):
        return a
    return b


def max(a, b):
    if(a < b):
        return b
    return a


[a, b, c, d] = [float(x) for x in input().split()]
flag = False
if(min(a, b) / max(a, b) == min(c, d) / max(c, d)):
    flag = True

if(min(a, c) / max(a, c) == min(b, d) / max(b, d)):
    flag = True

if(min(a, d) / max(a, d) == min(b, c) / max(b, c)):
    flag = True

if(flag):
    print("Possible")
else:
    print("Impossible")
