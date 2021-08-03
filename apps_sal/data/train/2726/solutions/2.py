def square_it(n):
    s = str(n)
    x = len(s)**.5
    if x % 1:
        return "Not a perfect square!"
    x = int(x)
    return '\n'.join(s[i:i + x] for i in range(0, len(s), x))
