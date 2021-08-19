li = list(map(int, input().split()))
(n, d) = (li[0], dict())
wealths = [None] + li[1:n + 1]
parents = li[n + 1:]
for k in list(range(1, n + 1)):
    d[k] = []
max_diff = -2 * int(100000000.0)
root = None
for i in range(len(parents)):
    if parents[i] != -1:
        d[parents[i]].append(i + 1)
    else:
        root = i + 1
q = [root]
indices = [0 for x in range(n + 1)]
while len(q) > 0:
    curr = d[q[-1]]
    if indices[q[-1]] < len(curr) and len(curr) >= 1:
        rn = curr[indices[q[-1]]]
        indices[q[-1]] += 1
        q.append(rn)
        for num in q:
            if num != rn:
                if wealths[num] - wealths[rn] > max_diff:
                    max_diff = wealths[num] - wealths[rn]
    else:
        q.pop(-1)
print(max_diff)
