n, x = list(map(int, input().split()))
for i in range(x):
    if(n == 0):
        break
    if(n % 10 == 0):
        n = n // 10
    else:
        n -= 1
print(n)
