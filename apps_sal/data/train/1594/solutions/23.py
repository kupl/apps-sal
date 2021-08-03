for _ in range(int(input())):
    n = int(input())
    power = []
    for i in range(n):
        power.append(input())
    d = True
    for i in range(n):
        if(power[i][i] != '1'):
            d = False
            break
    if(d):
        ans = (n * (n + 1)) // 2
        print(ans)
    else:
        print(0)
