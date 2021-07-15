t = int(input())
for z in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    mn = arr[-1]
    for i in range(n - 1, -1, -1):
        cnt += arr[i] > mn
        mn = min(arr[i], mn)
    print(cnt)
