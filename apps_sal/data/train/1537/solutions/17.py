prime=[False]*100000
nums=[1]
for i in range(2,100000):
    if(not prime[i]):
        nums.append(i)
        for j in range(i,8000,i):prime[j]=True
#print(nums)
t=int(input())
for _ in range(t):
    n=int(input())
    
    ans=0
    p=10**9+7
    for i in range(1,n+1):
        ans+=nums[nums[i]]
        if(ans>p):ans%=p
    print(ans)

