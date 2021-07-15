counter = -1
def flattree(node):
    nonlocal counter
    if visited[node]==1:
        return
    else:
        visited[node]=1
        counter += 1
        in_counter[node] = counter

        flat_tree[counter] = sweetness[node]

        for i in graph[node]:
            if visited[i]==0:
                flattree(i)
        counter += 1
        out_counter[node] = counter
        flat_tree[counter] = -sweetness[node]
    return


def getsum(BITTree, i):
    s = 0  # initialize result
    i = i + 1
    while i > 0:
        s += BITTree[i]
        i -= i & (-i)
    return s

def updatebit(BITTree, n, i, v):
    i += 1
    while i <= n:
        BITTree[i] += v
        i += i & (-i)

def construct(arr, n):
    BITTree = [0] * (n + 1)
    for i in range(n):
        updatebit(BITTree, n, i, arr[i])
    return BITTree

from collections import defaultdict
n = int(input())
sweetness = list(map(int, input().split()))
graph = defaultdict(list)

for i in range(n-1):
    n1, n2 = list(map(int, input().split()))
    graph[n1-1].append(n2-1)
    graph[n2-1].append(n1-1)

flat_tree = [0]*(2*n+1)
in_counter = [0]*n
out_counter = [0]*n
visited = [0]*n
flattree(0)
# print(flat_tree)
# print(in_counter)
# print(out_counter)
fenwicktree = construct(flat_tree, 2*n)

q = int(input())
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        node = query[1] - 1
        answer = getsum(fenwicktree, in_counter[node])
        print(answer)
    else:
        node = query[1]-1
        updatebit(flat_tree, (2*n), in_counter[node], query[2])
        updatebit(flat_tree, (2*n), out_counter[node], -query[2])

