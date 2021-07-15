
N,M = map(int,input().split())
dp = [0]*( (2*(10**5)) +1)
power = [0]*( (2*(10**5)) +1)
power[1] = 2
dp[1] = 2%int(M)
for i in range(2,int(N)+1):
    power[i] = (2*power[i-1])%int(M)


for i in range(2,int(N)+1):
    if(int(N)%i!=0):
        continue

    dp[i] = power[i]
    #print(power[i])
    for j in range(1,int(int(i)/2)+1):
        if(i%j==0):
            dp[i] = dp[i]-dp[j]
            if(dp[i]<0):
                dp[i] += int(M)
        
print(dp[int(N)]) 
