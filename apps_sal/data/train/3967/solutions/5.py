from itertools import product
def solve(a,b):
    res, start, stop = [], len(str(a)), len(str(b))+1
    for i in range(start, stop):
        res += ["".join(x) for x in product('538', repeat=i)]
    return sum(1 for x in res if a<=int(x)<=b and x.count('8')>=x.count('5')>=x.count('3'))
