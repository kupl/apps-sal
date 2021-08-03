from itertools import groupby

s = input()
n = len(s)
s = [s[i] for i in range(n)]
mod = 10**9 + 7

data = groupby(s)
data = [(key, len(list(group))) for key, group in data]
Start = 1
End = 1
if data[0][0] == "0":
    Start += data[0][1]
    data = data[1:]
if not data:
    print(Start - 1)
    return

if data[-1][0] == "0":
    End += data[-1][1]
    data.pop()

comp = [0] * len(data)
for i in range(len(data)):
    comp[i] = data[i][1]

n = len(comp)
if n == 1:
    print(comp[0] * Start * End)
    return

odd = [(comp[i], i // 2) for i in range(n) if i % 2 == 1]
# print(odd)
N = len(odd)
ID = [-1] * n
stack = []
for i in range(N):
    while stack and stack[-1][0] < odd[i][0]:
        stack.pop()
    if stack:
        ID[2 * i + 1] = stack[-1][1]
    stack.append(odd[i])

# print(ID[1::2])
dp = [0] * n
dp[0] = comp[0]
pre = [0] * n
for i in range(2, n, 2):
    id = ID[i - 1]
    if id == -1:
        res = comp[i - 1] * dp[i - 2]
        pre[i - 1] = res
        # prel[i-1]=1
    else:
        j = 2 * id + 1
        # res=(comp[i-1]*dp[i-2]+(comp[j]-comp[i-1])*premono[j])%mod
        res = (comp[i - 1] * dp[i - 2] + pre[j] - comp[i - 1] * dp[j - 1]) % mod
        pre[i - 1] = res
        # prel[i-1]=prel[j]+1
    dp[i] = (comp[i] * res + dp[i - 2] + comp[i]) % mod
# print(pre)
# print(dp)
print((dp[-1] * Start * End) % mod)
