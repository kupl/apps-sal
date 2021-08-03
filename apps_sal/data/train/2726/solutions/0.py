def square_it(digits):
    s = str(digits)
    n = len(s)**0.5
    if n != int(n):
        return "Not a perfect square!"
    n = int(n)
    return "\n".join(s[i * n:i * n + n] for i in range(int(n)))
