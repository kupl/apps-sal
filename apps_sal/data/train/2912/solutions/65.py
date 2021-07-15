def find_multiples(i, l):
    return list(range(i, l if not l%i==0 else l+i, i))
