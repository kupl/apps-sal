from collections import *


def solve():
    s = input()
    n = len(s)
    nxt = [[float('inf')] * (n + 10) for _ in range(26)]
    for i in range(n - 1, -1, -1):
        for j in range(26):
            nxt[j][i] = nxt[j][i + 1]
        nxt[ord(s[i]) - ord('a')][i] = i
    deq = deque()
    used = [False] * (n + 5)
    for i in range(26):
        if nxt[i][0] == float('inf'):
            print(chr(ord('a') + i))
            return
        deq.append((i, str(chr(ord('a') + i)), nxt[i][0]))
        used[nxt[i][0]] = True
    while True:
        siz = len(deq)
        for _ in range(siz):
            (i, pre, pos) = deq.popleft()
            for j in range(26):
                np = nxt[j][pos + 1]
                if np == float('inf'):
                    print(pre + str(chr(ord('a') + j)))
                    return
                if not used[np]:
                    used[np] = True
                    deq.append((j, pre + str(chr(ord('a') + j)), np))


solve()
