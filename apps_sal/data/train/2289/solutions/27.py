from collections import defaultdict
inf = 10**10
A = list(map(lambda x:ord(x)-ord('a'), list(input())))
N = len(A)
abc = 'abcdefghijklmbopqrstuvwxyz'
s_to_i = [[N]*26 for _ in range(N+1)]
for i in range(N)[::-1]:
    for x in range(26):
        s_to_i[i][x] = s_to_i[i+1][x]
    s_to_i[i][A[i]] = i
dp = [0]*(N+2)
dp[-2] = 1
for i in range(N)[::-1]:
    now = max(s_to_i[i])+1
    dp[i] = dp[now]+1
n = dp[0]
now = 0
ans = []
for i in range(n):
    for x in range(26):
        tmp = s_to_i[now][x]+1
        if dp[tmp] <= n-i-1:
            ans.append(chr(x+ord('a')))
            now = tmp
            break
print(*ans, sep = '')



    
        




