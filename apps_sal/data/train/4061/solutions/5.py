from fractions import gcd

def gn(n):
    prev = 7
    i = 2
    res = [1]
    while (i <= n):
        nou = prev + gcd(prev, i)
        res.append(nou - prev)
        prev = nou
        i += 1
    return res

def count_ones(n):
    a = [x for x in gn(n) if x == 1]
    return len(list(a))

def pn(n):
    prev = 7
    i = 2
    res = []
    cnt = 0
    while (cnt < n):
        nou = prev + gcd(prev, i)
        d = nou - prev
        if ((d != 1) and (d not in res)): 
            res.append(d)
            cnt += 1 
        prev = nou
        i += 1
    return res

def max_pn(n):
    return max(pn(n))

def an_overn(n):
    prev = 7
    i = 2
    res = []
    cnt = 0
    while (cnt < n): 
        nou = prev + gcd(prev, i)
        d = nou - prev
        if (d != 1):
            res.append(nou / i)
            cnt += 1 
        prev = nou
        i += 1
    return res

def an_over_average(n):
    a = an_overn(n)
    return int(sum(a) / len(a))

