(n, a) = list(map(int, input().split()))
for _ in range(a):
    if n == 0:
        break
    elif str(n)[-1] == '0':
        n = n // 10
    else:
        n = n - 1
print(str(n) + '\n')
