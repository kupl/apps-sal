class Tree():
    def __init__(self, n, edge, indexed=1):
        self.n = n
        self.tree = [[] for _ in range(n)]
        for e in edge:
            self.tree[e[0] - indexed].append(e[1] - indexed)
            self.tree[e[1] - indexed].append(e[0] - indexed)

    def setroot(self, root):
        self.root = root
        self.parent = [None for _ in range(self.n)]
        self.parent[root] = -1
        self.depth = [None for _ in range(self.n)]
        self.depth[root] = 0
        self.order = []
        self.order.append(root)
        stack = [root]
        while stack:
            node = stack.pop()
            for adj in self.tree[node]:
                if self.parent[adj] is None:
                    self.parent[adj] = node
                    self.depth[adj] = self.depth[node] + 1
                    self.order.append(adj)
                    stack.append(adj)

INF = 10**18

import sys
input = sys.stdin.readline

N = int(input())
E = [tuple(map(int, input().split())) for _ in range(N - 1)]

num = [None for _ in range(N)]

K = int(input())

for _ in range(K):
    v, p = map(int, input().split())
    num[v - 1] = p

tree = Tree(N, E)
tree.setroot(v - 1)

even = []
odd = []

for i in range(N):
    if num[i] is not None:
        if tree.depth[i] % 2 == 0:
            even.append(num[i] % 2)
        else:
            odd.append(num[i] % 2)

if not ((all(even) or not any(even)) and (all(odd) or not any(odd))):
    print('No')

else:
    I = [[-INF, INF] for _ in range(N)]
    for i in range(N):
        if num[i] is not None:
            I[i] = [num[i], num[i]]
    for node in tree.order[::-1]:
        lt, rt = I[node]
        for adj in tree.tree[node]:
            lt = max(lt, I[adj][0] - 1)
            rt = min(rt, I[adj][1] + 1)
        if lt > rt:
            print('No')
            break
        I[node] = [lt, rt]

    else:
        stack = [v - 1]
        visited = [0 for _ in range(N)]
        visited[v - 1] = 1
        while stack:
            node = stack.pop()
            for adj in tree.tree[node]:
                if visited[adj]:
                    continue
                visited[adj] = 1
                if I[adj][0] <= num[node] - 1 <= I[adj][1]:
                    num[adj] = num[node] - 1
                elif I[adj][0] <= num[node] + 1 <= I[adj][1]:
                    num[adj] = num[node] + 1
                else:
                    print('No')
                    break
                stack.append(adj)
            else:
                continue
            break
        else:
            print('Yes')
            print('\n'.join(map(str, num)))
