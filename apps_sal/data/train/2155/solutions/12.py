
from collections import defaultdict
def solve():

    n,m = list(map(int,input().split()))
    la = []
    for i in range(n):
        z = list(map(int,input().split()))
        la.append(z)

    dp1, dp2, dp3, dp4 = [[[0 for i in range(m+1)] for i in range(n+1)] for i in range(4)]

    for i in range(n):
        for j in range(m):
            dp1[i][j] = la[i][j]
            z1,z2 = 0,0
            if i-1>=0:
                z1 = dp1[i-1][j]
            if j-1>=0:
                z2 = dp1[i][j-1]

            dp1[i][j]+=max(z1,z2)

    for i in range(n-1,-1,-1):
        for j in range(m):
            dp2[i][j] = la[i][j]
            z1,z2 = 0,0
            if i+1<n:
                z1 = dp2[i+1][j]
            if j-1>=0:
                z2 = dp2[i][j-1]

            dp2[i][j]+=max(z1,z2)

    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            dp3[i][j] = la[i][j]
            z1,z2 = 0,0
            if i+1<n:
                z1 = dp3[i+1][j]
            if j+1<m:
                z2 = dp3[i][j+1]

            dp3[i][j]+=max(z1,z2)

    for i in range(n):
        for j in range(m-1,-1,-1):
            dp4[i][j] = la[i][j]
            z1,z2 = 0,0
            if i-1>=0:
                z1 = dp4[i-1][j]
            if j+1<m:
                z2 = dp4[i][j+1]

            dp4[i][j]+=max(z1,z2)

    ans = 0
    # print(dp1)
    # print(dp2)
    for i in range(1,n-1):
        for j in range(1,m-1):
            z1,z2,z3,z4 = dp1[i][j-1],dp2[i+1][j],dp3[i][j+1],dp4[i-1][j]

            ans = max(z1+z2+z3+z4,ans)
            z1,z2,z3,z4 = dp1[i-1][j],dp2[i][j-1],dp3[i+1][j],dp4[i][j+1]
            ans = max(z1+z2+z3+z4,ans)



            # print(ans)

    print(ans)




# t = int(stdin.readline())
# for _ in range(t):
solve()

