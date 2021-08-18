
__author__ = 'artyom'


def read_int():
    return int(input())


def read_int_ary():
    return map(int, input().split())


n = read_int()

g = [[] for x in range(n + 1)]
for i in range(n - 1):
    u, v = read_int_ary()
    g[u].append(v)
    g[v].append(u)

init = [0] + list(read_int_ary())
goal = [0] + list(read_int_ary())
s = []


def solve(graph, start):
    stack = [(start, -1, 0, [1, 1])]
    while stack:
        node, parent, sign, st = stack.pop(-1)
        if init[node] ^ st[sign] == goal[node]:
            s.append(node)
            st = list(st)
            st[sign] ^= 1
        sign ^= 1
        for child in graph[node]:
            if child != parent:
                stack.append((child, node, sign, st))


solve(g, 1)
print(len(s))
print('\n'.join(map(str, s)))
