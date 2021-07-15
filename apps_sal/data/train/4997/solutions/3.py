def sigma1(n):
    return sum(set(sum(([k, n//k] for k in range(2, int(n**0.5) + 1) if not n % k), [1, n])))

def equal_sigma1(limit):
    return sum(n for n in range(limit + 1) if n != int(str(n)[::-1]) and sigma1(n) == sigma1(int(str(n)[::-1])))
