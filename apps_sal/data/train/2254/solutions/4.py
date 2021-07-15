n,q = map(int,input().split())
xi = [[0]*(n+1) for i in range(2)]
noti = []
ans = ""
num = 0
num2 = 0
num3 = 0
while q > 0:
    typ,xt = map(int,input().split())
    if typ == 1:
        xi[0][xt] += 1
        noti += [xt]
        num += 1
        num2 += 1
    elif typ == 3:
        for i in range(num3,xt):
            if i+1 > xi[1][noti[i]]:
                xi[0][noti[i]] -= 1
                num -= 1
        num3 = max(num3,xt)
    else:
        num -= xi[0][xt]
        xi[0][xt] = 0
        xi[1][xt] = num2
    ans += str(num)
    ans += "\n"
    q -= 1
print(ans)
