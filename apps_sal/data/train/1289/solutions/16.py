def D(n): return n and (2 * n - 1) * D(n - 1) or 1
def N(n): return n and (4 * n * n - 8 * n + 3) * N(n - 2) + 7 * D(n - 2) or 1


n = eval(input())
for i in range(n):
    n = eval(input())
    print(D(n))
