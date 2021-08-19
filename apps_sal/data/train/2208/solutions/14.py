def find(people, N):
    dic = {}
    gr = [[] for _ in range(N + 1)]
    count = 0
    for (a, b) in people:
        (a, b) = sorted([a, b])
        if (a, b) in dic:
            count += 1
        else:
            dic[a, b] = 1
            gr[a] += [b]
            gr[b] += [a]
    checked = [0] * (N + 1)
    parent = [-1] * (N + 1)
    for i in range(1, N + 1):
        if checked[i] == 0:
            stack = [i]
            while stack:
                node = stack.pop()
                checked[node] = 2
                for v in gr[node]:
                    if parent[node] == v:
                        continue
                    if checked[v] == 2:
                        continue
                    if checked[v] == 1:
                        count += 1
                    else:
                        stack += [v]
                        parent[v] = node
                        checked[v] = 1
    return count


people = []
(n, k) = list(map(int, input().strip().split(' ')))
for _ in range(k):
    (a, b) = list(map(int, input().strip().split(' ')))
    people += [(a, b)]
print(find(people, n))
