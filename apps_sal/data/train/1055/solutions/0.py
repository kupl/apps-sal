m, n = [int(i) for i in input().split()]
arr = list(map(int, input().split()))
arr = sorted(arr, reverse=True)
ans = 0
w = 0
q = m
for m in range(q):
    if(arr[m] > n):
        w = 1
        break
    ans += 1 + (arr[m] * (arr[m] + 1)) // 2
    n -= arr[m]

if(n == 0):
    print(ans)
else:
    if(w == 1):
        print(ans + q - m + (n * (n + 1)) // 2)
    else:
        print(ans)
