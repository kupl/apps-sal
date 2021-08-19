a = list(map(lambda x: ord(x) - ord('a'), list(input())))
n = len(a)
m = 26
b = [1] * (n + 1)
prev = [n] * m
G = [[] for i in range(n + 1)]
for i in reversed(range(n)):
    ai = a[i]
    tmp = min((b[j] for j in prev))
    for j in prev:
        G[i].append(j)
    b[i] = tmp + 1
    prev[ai] = i
cnt = min((b[j] for j in prev))
edge = prev
ans = []
for _ in range(cnt):
    for (i, to) in enumerate(edge):
        if b[to] == cnt - _:
            ans.append(chr(ord('a') + i))
            edge = G[to]
            break
print(''.join(ans))
