import bisect
import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
s = list(input())
q = int(input())

char_idx = [[] for _ in range(26)]
for i in range(n):
    char_idx[ord(s[i])-ord('a')].append(i)
# print(char_idx)

query = [input().split() for _ in range(q)]
# print(query)

for t, a, b in query:
    if t=='1':
        i = int(a) - 1
        if s[i] == b:
            continue
        else:
            idx = bisect.bisect_left(char_idx[ord(s[i])-ord('a')], i)
            if char_idx[ord(s[i])-ord('a')][idx] == i:
                del char_idx[ord(s[i])-ord('a')][idx]
            bisect.insort_left(char_idx[ord(b)-ord('a')], i)
            s[i] = b
    else:
        l = int(a) - 1
        r = int(b) - 1
        ans = 0
        for i in range(26):
            if len(char_idx[i]) == 0:
                continue
            it = bisect.bisect_left(char_idx[i], l)
            if it < len(char_idx[i]) and char_idx[i][it] <= r:
                ans += 1
        print(ans)

