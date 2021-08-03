import sys
readline = sys.stdin.readline


class Node:
    def __init__(self, sigma, depth):
        self.end = False
        self.child = [None] * sigma
        self.depth = depth

    def __setitem__(self, i, x):
        self.child[i] = x

    def __getitem__(self, i):
        return self.child[i]


sigma = 2
root = Node(sigma, 0)


def add_trie(S):
    vn = root
    for cs in S:
        if vn[cs] is None:
            vn[cs] = Node(sigma, vn.depth + 1)
        vn = vn[cs]
    vn.end = True


ans = 0

N, L = map(int, readline().split())

for _ in range(N):
    S = list(map(int, readline().strip()))
    add_trie(S)

cnt = 0
stack = [root]
while stack:
    vn = stack.pop()
    for i in range(2):
        if vn[i] is None:
            r = L - vn.depth
            cnt ^= -r & r
        else:
            stack.append(vn[i])

print('Alice' if cnt else 'Bob')
