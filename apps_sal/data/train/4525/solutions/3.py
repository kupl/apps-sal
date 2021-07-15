def spread(n):
    i,r = 0,[0 for _ in range(12)]
    while sum(r) != n:
        r[i] += 1
        i = (i+1)%12
    return r

def check_challenge(n,c,m):
    d = dict(zip('January February March April May June July August September October November December'.split(),range(13)))
    arr = spread(n)
    if m == 'January': return 'You are on track.'
    if n == c: return 'Challenge is completed.'
    x = sum(arr[:d.get(m)])
    if x > c: return f'You are {x-c} behind schedule.'
    return f'You are {c-x} ahead of schedule!' if c-x!=0 else 'You are on track.'
