from collections import deque
stack = deque()
n = int(input())
links = [tuple(map(lambda x: int(x) - 1, input().split())) for i in range(n - 1)]
linked_to = [[] for i in range(n)]
for (x, y) in links:
    linked_to[x].append(y)
    linked_to[y].append(x)
init = list(map(lambda x: x == '1', input().split()))
goal = list(map(lambda x: x == '1', input().split()))
stack.append(0)
ops = 0
visited = [False] * n
parent = [n] * (n + 1)
was_swapped = [False] * (n + 1)
visited[0] = True


def xor(x, y):
    return x != y


def get_chld(i):
    for e in linked_to[i]:
        if e != parent[i]:
            yield e


while len(stack) > 0:
    c = stack.pop()
    for l in linked_to[c]:
        if not visited[l]:
            visited[l] = True
            parent[l] = c
            stack.append(l)
chosen = []
stack.append(0)
while len(stack) > 0:
    c = stack.pop()
    stack.extend(get_chld(c))
    was_swapped[c] = was_swapped[parent[parent[c]]]
    if xor(xor(init[c], goal[c]), was_swapped[c]):
        was_swapped[c] = not was_swapped[c]
        ops += 1
        chosen.append(c + 1)
print(ops, *chosen, sep='\n')
