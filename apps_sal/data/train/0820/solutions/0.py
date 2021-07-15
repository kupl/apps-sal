# cook your dish here
for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    colors = [0]*41; cost = [0]*41
    color = 0
    for i in range(n):
        cc,pp = list(map(int,input().split()))
        colors[cc] += 1
        cost[cc] += pp
    for i in colors:
        if i>0: color += 1
    dp2 = [[0]*41 for i in range(color+1)]
    dp2[0] = [1]*41
    for i in range(1,color+1):
        for j in range(1,41):
            dp2[i][j] = dp2[i][j-1]+dp2[i-1][j-1]*(2**colors[j]-1)
    dp1 = [[0]*41 for i in range(color+1)]
    for i in range(1,color+1):
        for j in range(1,41):
            dp1[i][j] = dp1[i][j-1]+dp1[i-1][j-1]*(2**colors[j]-1)+dp2[i-1][j-1]*cost[j]*(2**(colors[j]-1))
    num=den=0
    for i in range(m,color+1):
        num += dp1[i][40]
        den += dp2[i][40]
    print(num/den)
