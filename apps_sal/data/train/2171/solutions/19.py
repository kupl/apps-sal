from queue import LifoQueue


def intin():
    return list(map(int, input().split()))


def iin():
    return int(input())


def Ain():
    return list(map(int, input().split()))


mod = 1000000007
n = iin()
m = n + 1
v = [[] for i in range(m)]
p = [0] * m
for _ in range(n - 1):
    (a, b) = intin()
    v[a].append(b)
    v[b].append(a)
vis = [False] * m
flipped = [0] * m
flip = [0] * m
ans = []


def dfs(root):
    q = [root]
    while len(q) > 0:
        node = q.pop()
        vis[node] = True
        flipped[node] = flipped[p[p[node]]]
        if flipped[node] != flip[node]:
            flipped[node] ^= 1
            ans.append(node)
        for i in range(len(v[node])):
            son = v[node][i]
            if not vis[son]:
                q.append(son)
                p[son] = node


a = Ain()
b = Ain()
for i in range(n):
    flip[i + 1] = a[i] ^ b[i]
dfs(1)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
