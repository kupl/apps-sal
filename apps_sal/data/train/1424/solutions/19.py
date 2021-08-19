(n, a) = list(map(int, input().strip().split()))
for i in range(a):
    if n == 0:
        print(n)
        break
    if n % 10 == 0:
        n = n // 10
    else:
        n -= 1
print(n)
