n, m = list(map(int, input().split()))
ass = list(map(int,input().split()))

def done(a):
    return all(x < y for  (x,y) in zip(a[:-1], a[1:]))

maxops = m-1
minops = 0
while maxops > minops:
    cops = (maxops+minops)//2
    base = 0
    ok = True
    for a in ass:
        if base > a and (base - a) > cops:
            ok = False
            break
        elif (base - a) % m > cops:
            base = a
    if ok:
        maxops = cops
    else:
        minops = cops+1
print (maxops)


