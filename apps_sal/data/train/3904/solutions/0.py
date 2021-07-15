from itertools import product

def is_divisible_by_6(s):
    if s[-1] in '13579': return []
    ss = s.replace('*','{}')
    return [ v for v in (ss.format(*p) for p in product(*(['0123456789']*s.count('*')))) if not int(v)%6]
