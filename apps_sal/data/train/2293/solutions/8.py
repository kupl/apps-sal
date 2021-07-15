n = int(input())
a = list(map(int,input().split()))

dp = [[ai,0,i,-1] for i,ai in enumerate(a)]

for i in range(1,2**n):
    for j in range(n):
        if(i >> j)&1:
            x = dp[i]
            y = dp[i - (1<<j)]
            if(x[0] < y[0] ):
                x,y = y,x
            m1 = x[0]
            i1 = x[2]
            if(x[2] == y[2]):                
                if(x[1] > y[1]):
                    m2 = x[1]
                    i2 = x[3]
                else:
                    m2 = y[1]
                    i2 = y[3]
            else:
                if(x[1] > y[0]):
                    m2 = x[1]
                    i2 = x[3]
                else:
                    m2 = y[0]
                    i2 = y[2]
            dp[i] = [m1,m2,i1,i2]

ans = [0]
for i in range(1,2**n):
    tmp = sum(dp[i][:2])
    ans.append(max(ans[-1],tmp))

print('\n'.join(map(str,ans[1:])))
