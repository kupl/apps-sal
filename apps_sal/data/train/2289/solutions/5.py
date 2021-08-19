import bisect
A = input()
n = len(A)
ch = [[] for _ in range(26)]
idx = []
used = set()
for i in range(n - 1, -1, -1):
    a = A[i]
    ch[ord(a) - ord('a')].append(i)
    used.add(a)
    if len(used) == 26:
        idx.append(i)
        used = set()
k = len(idx)
idx = idx[::-1]
for j in range(26):
    ch[j] = ch[j][::-1]
ans = ''
now = -1
for i in range(k):
    for j in range(26):
        nxt = ch[j][bisect.bisect_right(ch[j], now)]
        if nxt >= idx[i]:
            now = nxt
            ans += chr(j + ord('a'))
            break
for j in range(26):
    l = bisect.bisect_right(ch[j], now)
    if l == len(ch[j]):
        ans += chr(j + ord('a'))
        break
print(ans)
