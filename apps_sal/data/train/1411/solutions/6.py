t = int(input())
while(t != 0):
    rounds, r, x, y = list(map(int, input().split()))
    rv = abs(x - y)
    mv = max(x, y)
    ans = rounds * (rv / mv)
    if(ans - int(ans) == 0):
        print(int(ans) - 1)
    else:
        print(int(ans))
    t = t - 1
