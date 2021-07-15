def fibfusc(n, num_digits=None):
    if n < 2: return (1 - n, n)
    b = bin(n)[2:]
    
    x, y = fibfusc(int(b[0]))
    for bit in b[1:]:
        if bit == "1":
            x, y = (-y*(2*x + 3*y), (x + 2*y)*(x + 4*y))
        else:
            x, y = ((x + y) * (x - y), y * (2*x + 3*y))
        if num_digits:
            x, y = x % 10 ** num_digits - 10**num_digits, y % 10 ** num_digits
    return x, y

