n, a = map(int, input().split())
while(a):
    a = a - 1
    if n % 10 == 0:
        n = n // 10
    else:
        n = n - 1
    if n == 0:
        break
print(n)
