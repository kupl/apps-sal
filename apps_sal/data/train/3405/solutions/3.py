from itertools import permutations as p

n_str = '123456789'
formt = lambda n: sorted(list(map(''.join, list(filter(set, p(n_str, n))))))
db = formt(1) + formt(2) + formt(3) + formt(4) + formt(5)
hs = {1:0, 2:9, 3:81, 4:585, 5:3609}

def next_pandigital(lp):
    if lp in db:
        return db[db.index(lp):]
    while 1:
        lp = str(int(lp) + 1)
        if lp in db[hs[len(lp)]:]:
            break
    return db[db.index(lp):]

def is_pandigital(lp):
    return len(set(lp)) == len(lp) and '0' not in lp

def pow_root_pandigit(val, n, k):
    l = []
    low = int(val ** (1 / n) + 0.0001) + 1
    for p in next_pandigital(str(low)):
        v = int(p) ** n
        if is_pandigital(str(v)):
            l.append([int(p), v])
        if len(l) == k:
            return l
    return l[0] if len(l) == 1 else l
