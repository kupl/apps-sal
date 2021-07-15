from itertools import product as p
def is_divisible_by_6(s):
    return [u for u in [s.replace('*','{}').format(*x) for x in list(p(range(10),repeat=s.count('*')))] if int(u)%6==0]
