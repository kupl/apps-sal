N = int(input())
for _ in range(N):
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    count = 0
    last = 0
    for i in range(n):
        if arr[i] != 0:
            break
        last = i
        count += 1
    for i in arr[-1:last:-1]:
        if i != 0:
            break
        count += 1
    ans = n - count
    if ans == 0:
        print(1)
    else:
        print(ans)
