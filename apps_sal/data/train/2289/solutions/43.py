S=input()
N=len(S)
a=ord('a')
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
K=[[N]*(N+1) for i in range(26)]
for i in range(N-1,-1,-1):
    x=ord(S[i])-a
    for j in range(26):
        if j==x:
            K[j][i]=i
            continue
        K[j][i]=K[j][i+1]
dp=[0]*(N+2)
L=[0]*(N+2)
dp[N]=1
for i in range(N-1,-1,-1):
    c=0
    b=2*N
    for j in range(26):
        t=K[j][i]
        if b>dp[t+1]+1:
            b=dp[t+1]+1
            c=t+1
    dp[i]=b
    L[i]=c
X=dp[0]
t=0
ans=''
while X>1:
    t=L[t]
    ans+=S[t-1]
    X-=1
    #print(t,X,ans)
for j in range(26):
    if K[j][t] ==N:
        ans+=alpha[j]
        break
print(ans)



