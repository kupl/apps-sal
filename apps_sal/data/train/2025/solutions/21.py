def Prime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return 0
    return 1


n = int(input())
ans = []
for i in range(2, n + 1):
    if Prime(i):
        ans += [str(i)]
        t = i
        while t * i <= n:
            t *= i
            ans += [str(t)]
print(len(ans))
print(' '.join(ans))
