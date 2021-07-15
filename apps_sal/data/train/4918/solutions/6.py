def convert(n):
    b = 1
    s = 0
    while n > 0:
        if n % 10 == 1: s += b
        n //= 10
        b *= 1j
    return [int(s.real), int(s.imag)]
    

