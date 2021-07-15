import sys
import math

input = sys.stdin.readline
N, M = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]
connected = [set() for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    connected[a].add(b)
    connected[b].add(a)
for i in range(N):
    connected[i].add(i)

whole_set = set(range(N))
unconnected = [whole_set-connected[i] for i in range(N)]
assign = [-1] * N
ass_q = []
g = 0
for i in range(N):
    if len(unconnected[i]) != 0:
        assign[i] = g
        for j in unconnected[i]:
            assign[j] = (assign[i] + 1) % 2 + g
            ass_q.append(j)
        break
while len(ass_q) > 0:
    i = ass_q.pop()
    for j in unconnected[i]:
        if assign[j] == -1:
            assign[j] = (assign[i] + 1) % 2 + g
            ass_q.append(j)
        elif assign[j] == assign[i]:
            print((-1))
            return
    if len(ass_q) == 0:
        g += 2
        for i in range(N):
            if len(unconnected[i]) > 0 and assign[i] == -1:
                assign[i] = g
                for j in unconnected[i]:
                    assign[j] = (assign[i] + 1) % 2 + g
                    ass_q.append(j)
                break


groups = [(assign.count(g_), assign.count(g_+1)) for g_ in range(0, g, 2)]
ans = math.inf
not_assign = assign.count(-1)
for b in range(pow(2, len(groups))):
    taka, hashi = 0, 0
    for i in range(len(groups)):
        taka += groups[i][(b>>i)&1]
        hashi += groups[i][((~b)>>i)&1]
    for _ in range(not_assign):
        if taka < hashi:
            taka += 1
        else:
            hashi += 1
    ans = min(ans, (taka*(taka-1))//2 + (hashi*(hashi-1))//2)
print(ans)

