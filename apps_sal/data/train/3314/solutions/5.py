def solve(a,b):
    k = 2
    while k <= int(b**0.5):
        while b%k == 0:
            b //= k
            if a%k != 0: return False
        k += 1
    return a%b == 0

