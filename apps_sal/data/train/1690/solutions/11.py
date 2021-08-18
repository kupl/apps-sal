from collections import defaultdict


def friend(i, j, k):
    counter = 0
    for num in ids[i]:
        if (j, num) in insieme:
            counter += 1
        if counter == k:
            break
    if counter == k:
        return True
    return False


n, k = map(int, input().split())
ids = []
insieme = set()
for i in range(n):
    id = list(map(int, input().split()))
    id = id[1:]
    for el in id:
        insieme.add((i, el))
    ids.append(id)
graph = defaultdict(lambda: [])
for i in range(n - 1):
    for j in range(i + 1, n):
        if friend(i, j, k):
            graph[i].append(j)
            graph[j].append(i)
visited = [0] * n
visited[0] = 1
stack = [0]
counter = 1
while len(stack) > 0:
    u = stack.pop()
    for v in graph[u]:
        if visited[v] == 0:
            visited[v] = 1
            stack.append(v)
            counter += 1
print(counter)
