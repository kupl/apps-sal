t = int(input())
while(t):
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    for i in range(len(l)):
        ans = (ans ^ l[i])

    print(ans)
    t -= 1
