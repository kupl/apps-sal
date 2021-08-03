t = int(input())
for p in range(t):
    n = int(input())
    cnt = 0
    arr = list(map(int, input().split()))
    for i in range(n):
        if arr[i] >= n // 2:
            cnt += 1
    print(cnt)
