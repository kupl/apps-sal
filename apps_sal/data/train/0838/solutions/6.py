t = int(input())
while(t > 0):
    n = int(input())
    l = list(map(int, input().split()))
    ans = l[0]
    for i in range(1, n):
        ans = max(ans, l[i] + i)
    print(ans)
    t -= 1
