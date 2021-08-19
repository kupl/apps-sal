def convert(n):
    result = sum((1j ** i for (i, x) in enumerate(str(n)[::-1]) if x == '1'))
    return [result.real, result.imag]
