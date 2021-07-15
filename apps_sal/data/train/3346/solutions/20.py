import math
def gap(g, m, n):
    gapn = []
    prevprime = 0
    for i in range(m, n + 1):
        for j in range(2, int(math.ceil(i**0.5) + 1)):   
            if (i % j) == 0:
                break
        else:
            if prevprime > 0 and i - prevprime == g:
                gapn.append(prevprime)
                gapn.append(i)
                break
            prevprime = i
    if len(gapn) > 0:
        return gapn
    else:
        return None

