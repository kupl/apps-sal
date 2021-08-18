
t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        if(ans >= l[i]):
            ans += 1
        else:
            break
    print(ans)
