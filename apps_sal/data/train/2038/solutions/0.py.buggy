import sys

n, m = [int(x) for x in input().split()]

adj_for = [[] for _ in range(n)]
adj_back = [[] for _ in range(n)]

for _ in range(m):
    a, b = [int(x) for x in sys.stdin.readline().split()]
    a -= 1
    b -= 1
    adj_for[a].append(b)
    adj_back[b].append(a)


lens = [len(adj_back[i]) for i in range(n)]
stack = [x for x in range(n) if lens[x] == 0]
toposort = [x for x in range(n) if lens[x] == 0]

while len(stack):
    cur = stack.pop()
    for nb in adj_for[cur]:
        lens[nb] -= 1
        if lens[nb] == 0:
            toposort.append(nb)
            stack.append(nb)

if len(toposort) != n:
    print(-1)
    return

min_above = list(range(n))
min_below = list(range(n))

for i in toposort:
    for j in adj_back[i]:
        if min_above[j] < min_above[i]:
            min_above[i] = min_above[j]

for i in reversed(toposort):
    for j in adj_for[i]:
        if min_below[j] < min_below[i]:
            min_below[i] = min_below[j]

qt = ["A" if min_below[i] == min_above[i] == i else "E" for i in range(n)]

# qt = [None for x in range(n)]
#
# for i in range(n):
#     if qt[i] is not None:
#         continue
#     qt[i] = 'A'
#     stack_for = [i]
#     while len(stack_for):
#         cur = stack_for.pop()
#         for nb in adj_for[cur]:
#             if qt[nb] is None:
#                 qt[nb] = 'E'
#                 stack_for.append(nb)
#
#
#     stack_back = [i]
#     while len(stack_back):
#         cur = stack_back.pop()
#         for nb in adj_back[cur]:
#             if qt[nb] is None:
#                 qt[nb] = 'E'
#                 stack_back.append(nb)
#
print(len([x for x in qt if x == 'A']))
print("".join(qt))
