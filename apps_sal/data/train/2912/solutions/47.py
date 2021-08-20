def find_multiples(integer, limit):
    n = 1
    mults = []
    while integer * n <= limit:
        mults.append(integer * n)
        n += 1
    return mults
