def nextPowerOf2(n, p):
    if n and (not n & n - 1):
        return n
    while p < n:
        p <<= 1
    return p


for _ in range(int(input())):
    print(nextPowerOf2(int(input()), 1))
