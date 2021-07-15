out = [1, 5, 6]

def green(n):
  
    f = 5
    s = 6
    q = 1

    while n >= len(out):
        q = 10 * q
        f = f**2 % q
        s = (1 - (s - 1)**2) % q
        out.extend(sorted(j for j in [f, s] if j not in out))
    return out[n-1]
