import itertools
def sflpf(n):
    f = 2
    l = []
    increments = itertools.chain([1,2,2], itertools.cycle([4,2,4,2,4,6,2,6]))
    for incr in increments:
        if f*f > n:
            break
        while n % f == 0:
            l.append(f)
            n //= f
        f += incr
    if n > 1:
        l.append(n)
    return min(l) + max(l) if len(l) > 1 else 0       
    
def sflpf_data(val, nMax):
    return [i for i in range(4, nMax + 1) if sflpf(i) == val]

