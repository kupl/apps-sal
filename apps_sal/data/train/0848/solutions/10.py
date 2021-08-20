t = int(input())
while t > 0:
    n = int(input())
    li = list(map(int, input().strip().split()))[:n]
    sum = 0
    start = 0
    end = 3 - 1
    for i in range(3):
        sum += li[i]
    ans = sum
    for i in range(3, n + 3):
        sum += li[i % n] - li[(i - 3) % n]
        if sum > ans:
            ans = sum
            start = (i - 3 + 1) % n
            end = i % n
    print(ans)
    t = t - 1
