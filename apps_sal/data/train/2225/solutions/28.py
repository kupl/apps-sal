import sys
from collections import deque
sys.setrecursionlimit(10000)
INF = float('inf')
(N, L) = list(map(int, input().split()))
S = set()
for _ in range(N):
    S.add(input())


def grundy(size):
    """
    :param int size: 候補の長さ
    :return:
    """
    i = 1
    while (L - size + 1) % i == 0:
        i *= 2
    return i // 2


trie = {}
for s in S:
    t = trie
    for c in s:
        if c not in t:
            t[c] = {}
        t = t[c]
ok_size_list = []
children = deque()
children.append((trie, 0))
while len(children) > 0:
    (node, size) = children.popleft()
    if len(node) == 1:
        ok_size_list.append(size + 1)
    for (c, child) in node.items():
        children.append((child, size + 1))
g = 0
for size in ok_size_list:
    g ^= grundy(size)
if g != 0:
    print('Alice')
else:
    print('Bob')
