def movie(c, t, p):
    s = c
    n = 1 
    while True:
        summation = (1 - p**(n+1))/(1-p) - 1
        if int(s + t*summation)+1 < n*t:
            break
        n += 1
    return n

