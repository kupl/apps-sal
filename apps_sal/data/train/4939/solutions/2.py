CAFE, DECAF = 51966, 912559
def coffee_limits(y, m, d):
    n = int(''.join([str(y), str(m).zfill(2), str(d).zfill(2)]))
    A = lambda x : next((i for i in range(1,5001) if 'dead' in hex(n+(i*x))[2:]),0)
    return [A(CAFE), A(DECAF)]
