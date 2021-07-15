def ever(n):
    s = str(n)
    C = [s.count('3'), s.count('5'), s.count('8')]
    if sum(C)==len(s) and sorted(C)==C :
        return True
    return False

D={i for i in range(1000000) if ever(i)}


def solve(a,b):
    return len({e for e in D if e>=a and e<=b})
