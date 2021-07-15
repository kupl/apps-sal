def convert(n):
    res = sum(x * 1j**i for i,x in enumerate(map(int, str(n)[::-1])))
    return [res.real, res.imag]
