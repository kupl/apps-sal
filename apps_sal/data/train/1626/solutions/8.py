from math import sqrt, ceil, log10
import numpy as np


def getGreatest(n, d, prefix):
    rows = 9 * 10**(d - 1)
    triangle = rows * (d + rows * d) // 2
    l = 0
    r = triangle

    while l < r:
        mid = l + ((r - l) >> 1)
        triangle = mid * prefix + mid * (d + mid * d) // 2
        prevTriangle = (mid - 1) * prefix + (mid - 1) * (d + (mid - 1) * d) // 2
        nextTriangle = (mid + 1) * prefix + (mid + 1) * (d + (mid + 1) * d) // 2

        if triangle >= n:
            if prevTriangle < n:
                return prevTriangle
            else:
                r = mid - 1
        else:
            if nextTriangle >= n:
                return triangle
            else:
                l = mid
    return l * prefix + l * (d + l * d) // 2


def findDiff(n, x):
    #print("Xdiff=", x)
    mult = 1
    temp = x / 10
    while temp >= 1:
        temp /= 10
        mult *= 10
  #  print("sectionMATT=", calcSeq(mult-1))
    #print("rowMATT=", calcSeq(x-(mult-1)) )
    sLen = x - (mult - 1)
    d = round(log10(mult))
   # print("WOW, slen is", sLen)
    prefixes = 0
    for z in range(1, round(d) + 1):
        prefixes += (9 * z * 10**(z - 1))
    #    print('PROIFFIXES=',prefixes)
    #print('now N IS THIS ONE? WRONG YET??: NOPE!!!!', n)
    #print("PREFIXED", prefixes)
    d += 1
    # print('D',d)
   # totEX = int((d + d*(sLen)))
  #  ort = d*sLen/2*(1+sLen)
    n -= calcSeq(mult - 1)
   # print('ave Len=', int(d + d*(sLen)), d, sLen )
    #print("pewpewpew, totEXSHOULDNT BE TOO BIG=",int(totEX*sLen/2), calcSeq(mult-1))
    temp = getGreatest(n, d, prefixes)
    #print("temp=", temp)
    # print("DDDD=",d)
    #print('theN=', n)

    #print('theN=', n)
   # n -= totC
    # n = int(n/2  + (n - totEX*sLen)/2)#int((int(totEX)*sLen)/2)
    # for _ in range(sLen+1):
    #    n -= int(d*sLen/2)
#    print('theN=', n)
    return n - temp


def calcSeq(current):
    x = np.int64(current * (current + 1) / 2)
    mult = 10
    temp = np.int64(current)
    while temp > 0:
        temp = current
        temp -= mult - 1
        mult *= 10
        if temp > 0:
            x += np.int64(temp * (temp + 1) / 2)
    return x


def solve(n):
  #  print([calcSeq(x) for x in [0,9,99,999]])

    maxN = n
    minN = 0
    x = float(0)
    delta = 2
    prev = 0
    current = round(sqrt(2 * n))
    prevRight = True
    while maxN - minN > 1:
        x = calcSeq(current)
        delta = abs(current - prev)
        prev = current
        if x < n and prevRight:
            current += ceil((maxN - current) / 2)
            prevRight = True
        elif x < n:
            minN = current
            current += ceil((maxN - current) / 2)
            prevRight = True
        elif x > n and prevRight == False:
            maxN = current
            current -= round((current - minN) / 2)
            prevRight = False
        elif x > n:
            current -= round((current - minN) / 2)
            prevRight = False
        else:
            maxN = current
            minN = current - 1
    if calcSeq(current) < n:
        current += 1
    prev = current - 1

    element = findDiff(n, prev)
    nDigits, nines = 1, 9
    total = float(nDigits * nines)
    while total < element:
        nDigits += 1
        nines *= 10
        total += nDigits * nines

    total -= nDigits * nines
    element2 = element - total
    start = 10**(nDigits - 1)
    number = str(start + ceil(element2 / nDigits) - 1)

    return int(number[(int(element2) - 1) % nDigits])
