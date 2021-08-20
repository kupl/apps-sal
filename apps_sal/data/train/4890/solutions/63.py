def find_difference(a, b):
    (av, bv) = (1, 1)
    for i in a:
        av *= i
    for i in b:
        bv *= i
    return av - bv if av >= bv else bv - av
