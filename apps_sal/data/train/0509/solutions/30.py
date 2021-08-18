from queue import Queue
N, M = map(int, input().split())
P = [-1] * (N + 1)
Visited = [False] * (N + 1)
Past = [[] for i in range(N + 1)]
for i in range(M):
    u, v, c = map(int, input().split())
    Past[u].append((v, c))
    Past[v].append((u, c))


q = Queue()
q.put(1)
P[1] = 1
while not q.empty():
    st = q.get()
    for to, c in Past[st]:
        if P[to] == -1:
            if P[st] == c:
                P[to] = c + 1 if c + 1 <= N else 1
            else:
                P[to] = c
            q.put(to)

flag = True
for i in range(1, N + 1):
    if P[i] == -1:
        flag = False

if flag:
    for i in range(1, N + 1):
        print(P[i])
else:
    print("No")
