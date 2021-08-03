def squares(x, n):
    mx = [x]
    while len(mx) < n:
        mx.append(mx[-1]**2)
    return mx if n > 0 else []
