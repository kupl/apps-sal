import sys
input = sys.stdin.buffer.readline
n = int(input())
a = list(map(int,input().split()))
n = max(a)+1
spf = [i for i in range(n)]
for i in range(4,n,2): spf[i] = 2
for i in range(3,int(n**.5)+1,2):
    if spf[i]!=i:continue
    for j in range(i*i, n, i):
        if spf[j]==j:spf[j] = i
cnt = 0
dp = [0]*n
for i in range(1,n):
    if spf[i]==i: cnt+=1
    dp[i] = cnt
def query(n):
    return dp[n]-dp[int(n**.5)]+1
print("\n".join(str(dp[n]-dp[int(n**.5)]+1) for n in a))

