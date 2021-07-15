def find(r):
    dict = {i: 2**i for i in range(10)}
    return sum(dict.get(y) for y in r)
