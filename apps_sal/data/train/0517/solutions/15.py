
powers=[0 for i in range(150001)]

def factorize(n):
    factors=set()
    for i in range(1,n):
        if i*i>n:
            break
        else:
            if (n%i)==0:
                factors.add(i)
                factors.add(n//i)
    factors.remove(n)
    return factors

def calc(m):
    powers[0]=1
    for i in range(1,150001):
        powers[i]=(powers[i-1]*2)%m

n,m=list(map(int,input().split()))
calc(m)
dp=[0 for i in range(n+1)]
dp[1]=2
for i in range(2,n+1):
    factors=factorize(i)
    dp[i]=powers[i]
    for num in factors:
        dp[i]-=dp[num]
        dp[i]=(dp[i]+m)%m
print(dp[n])

