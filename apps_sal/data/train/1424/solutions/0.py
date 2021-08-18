n, a = map(int, input().split())
for i in range(a):
    if(n % 10 == 0):
        n = n // 10
    else:
        n = n - 1

print(n)
