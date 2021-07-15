import sys
sys.setrecursionlimit(10**6)

a = input() + "$"
n = len(a)

alph = "abcdefghijklmnopqrstuvwxyz"
dp = [-1] * (n + 1)

next_ = [[-1] * (n + 1) for i in range(26)]
for char in range(26):
    tmp = - 1
    for i in range(n)[::-1]:
        if a[i] == alph[char]:
            tmp = i + 1
        next_[char][i] = tmp


def solve():
    for i in range(n + 1)[::-1]:
        tmp = n + 1
        for char in range(26):
            if next_[char][i] == -1:
                dp[i] = 1
                break
            tmp = min(dp[next_[char][i]] + 1 , tmp)
        else:
            dp[i] = tmp

solve()
ans = []
i = 0
while True:
    for char in range(26):
        if next_[char][i] == -1:
            ans.append(alph[char])
            print("".join(ans))
            return
        if dp[i] == dp[next_[char][i]] + 1:
            ans.append(alph[char])
            i = next_[char][i]
            break
