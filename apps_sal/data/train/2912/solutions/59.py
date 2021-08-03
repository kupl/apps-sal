def find_multiples(integer, limit):
    mults = []
    n = integer
    while n <= limit:
        mults.append(n)
        n = n + integer
    return mults
