def find_key(key):
    n = int(key, 16)
    a, b = factor(n)
    return (a - 1) * (b - 1)

def factor(n):
    for i in range(2, n):
        if n % i == 0:
            return i, int(n/i)
