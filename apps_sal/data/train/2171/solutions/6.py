# 429A

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


# def solve(graph, level, state, node, parent=-1):
# t = level % 2
# st = list(state)
# if init[node] ^ st[t] == goal[node]:
#     s.append(node)
#     st[t] = 1 - st[t]
#   for child in graph[node]:
#     if child != parent:
#       solve(graph, level + 1, st, child, node)


def solve(graph, start):
    stack = [(start, -1, [1, 1], 0)]
    while stack:
        params = stack.pop(-1)
        node = params[0]
        parent = params[1]
        st = list(params[2])
        sign = params[3]
        if init[node] ^ st[sign] == goal[node]:
            s.append(node)
            st[sign] ^= 1
        sign ^= 1
        for child in graph[node]:
            if child != parent:
                stack.append((child, node, st, sign))


solve(g, 1)
print(len(s))
for v in s:
    print(v)
