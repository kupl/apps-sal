# cook your dish here
def optimized(x, y, n):
    if x == y:
        return 0
    p = (x ^ y).bit_length()
    diff = pow(2, p)
    n = n + 1
    ans = (n // diff) * (diff // 2)
    if x < y:
        return ans + (n % diff if n % (diff) < diff // 2 else (diff // 2))
    else:
        return ans + (n % diff - (diff // 2) if n % (diff) > diff // 2 else 0)


for test in range(int(input())):
    x, y, n = map(int, input().split())
    print(optimized(x, y, n))
