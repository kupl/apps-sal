from bisect import bisect_left
A = [ord(i) - 97 for i in input()]
A = A + list(range(26))
A = A[::-1]
dp = [0] * 26
key = [[] for _ in range(26)]
val = [[] for _ in range(26)]
for (i, a) in enumerate(A):
    x = min(dp) + 1
    dp[a] = x
    key[a].append(i)
    val[a].append(x)
ret = ''
x = dp[dp.index(min(dp))] + 1
pos = 10 ** 6
while True:
    for i in range(26):
        if key[i][0] < pos:
            j = bisect_left(key[i], pos) - 1
            if val[i][j] == x - 1:
                ret += chr(i + 97)
                pos = key[i][j]
                x -= 1
                break
    else:
        break
print(ret)
