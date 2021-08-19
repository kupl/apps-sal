"""while test:
    solve()
    test-=1"""
n = [int(i) for i in input().split()]
x = n[1]
n = n[0]
for i in range(x):
    if n == 0:
        break
    if n % 10 == 0:
        n = n // 10
        continue
    n = n - 1
print(n)
