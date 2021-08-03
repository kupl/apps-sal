
T = int(input().strip('\n'))

for t in range(T):
    n, k = list(map(int, input().strip('\n').split()))
    if k > n:
        print(0)
        continue
    k = min(k, n - k)
    ans = 1
    for i in range(k):
        ans *= n - i
        ans /= i + 1
    print(ans)
