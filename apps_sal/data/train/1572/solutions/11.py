from collections import defaultdict
list1 = list(map(int, input().split()))
N = list1[0]
list1.pop(0)
wealth = []
parent = {}
children = defaultdict(list)
for i in range(N):
    wealth.append(list1[0])
    list1.pop(0)
root = 0
for j in range(N):
    if list1[j] != -1:
        parent[j] = list1[j] - 1
        children[list1[j] - 1].append(j)
    else:
        root = j
leaves = []
dowegoup = {}
tobevisited = [root]
while len(tobevisited) > 0:
    temp = tobevisited.pop()
    if len(children[temp]) == 0:
        leaves.append(temp)
    else:
        for i in range(len(children[temp])):
            tobevisited.append(children[temp][i])
            if wealth[children[temp][i]] > wealth[temp]:
                dowegoup[children[temp][i]] = False
            else:
                dowegoup[children[temp][i]] = True
visited = {}
disparity = {}
answer = -10**10
for j in range(len(leaves)):
    disparity[leaves[j]] = 0
while len(leaves) > 0:
    temp = leaves.pop(0)
    if parent[temp] not in disparity:
        disparity[parent[temp]] = wealth[parent[temp]] - wealth[temp]
        if disparity[temp] > 0:
            disparity[parent[temp]] += disparity[temp]
    else:
        if disparity[temp] > 0:
            gladiator = wealth[parent[temp]] - wealth[temp] + disparity[temp]
        else:
            gladiator = wealth[parent[temp]] - wealth[temp]
        disparity[parent[temp]] = max(gladiator, disparity[parent[temp]])
    if parent[temp] != root:
        visited[parent[temp]] = True
        leaves.append(parent[temp])
    if disparity[parent[temp]] > answer:
        answer = disparity[parent[temp]]
print(answer)
