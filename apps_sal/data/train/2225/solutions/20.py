import sys
sys.setrecursionlimit(100000)


def dfs(cur, dep=0):
    if cur == -1:
        x = l - dep
        return x & -x
    return dfs(trie[cur][0], dep + 1) ^ dfs(trie[cur][1], dep + 1)


(n, l) = list(map(int, input().split()))
trie = [[-1, -1] for _ in range(100001)]
idx = 1
for s in (input() for _ in range(n)):
    cur = 0
    for c in map(int, s):
        if trie[cur][c] == -1:
            trie[cur][c] = idx
            idx += 1
        cur = trie[cur][c]
xor = dfs(trie[0][0]) ^ dfs(trie[0][1])
print('Alice' if xor else 'Bob')
