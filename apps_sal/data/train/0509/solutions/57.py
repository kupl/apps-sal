import collections as co
(n, m) = list(map(int, input().split()))
ansDic = dict()
edgeLis = [[] for i in range(n + 1)]
for i in range(1, n + 1):
    ansDic[i] = 0
for i in range(1, m + 1):
    edge = list(map(int, input().split()))
    edgeLis[edge[0]].append([edge[1], edge[2]])
    edgeLis[edge[1]].append([edge[0], edge[2]])
q = co.deque()
q.append(1)
while len(q) > 0:
    k = q.popleft()
    if ansDic[k] == 0:
        ansDic[k] = k
    for lis in edgeLis[k]:
        l1 = lis[0]
        l2 = lis[1]
        if ansDic[l1] == 0:
            q.append(l1)
            if ansDic[k] != l2:
                ansDic[l1] = l2
            elif l1 != l2:
                ansDic[l1] = l1
            else:
                ansDic[l1] = k
for i in range(1, n + 1):
    print(ansDic[i])
