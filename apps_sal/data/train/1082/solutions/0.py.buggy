from collections import defaultdict
counter = -1


def flattree(node):
    nonlocal counter
    if visited[node] == 1:
        return
    else:
        visited[node] = 1
        counter += 1
        i_c[node] = counter

        flat_tree[counter] = swt[node]

        for i in graph[node]:
            if visited[i] == 0:
                flattree(i)
        counter += 1
        o_c[node] = counter
        flat_tree[counter] = -swt[node]
    return


def getsum(BITTree, i):
    s = 0  # initialize result
    i = i + 1
    while i > 0:
        s += BITTree[i]
        i -= i & (-i)
    return s


def upd(BITTree, n, i, v):
    i += 1
    while i <= n:
        BITTree[i] += v
        i += i & (-i)


def construct(arr, n):
    BITTree = [0] * (n + 1)
    for i in range(n):
        upd(BITTree, n, i, arr[i])
    return BITTree


n = int(input())
swt = list(map(int, input().split()))
graph = defaultdict(list)

for i in range(n - 1):
    n1, n2 = list(map(int, input().split()))
    graph[n1 - 1].append(n2 - 1)
    graph[n2 - 1].append(n1 - 1)

flat_tree = [0] * (2 * n + 1)
i_c = [0] * n
o_c = [0] * n
visited = [0] * n
flattree(0)

tre = construct(flat_tree, 2 * n)

q = int(input())
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        node = query[1] - 1
        answer = getsum(tre, i_c[node])
        print(answer)
    else:
        node = query[1] - 1
        upd(flat_tree, (2 * n), i_c[node], query[2])
        upd(flat_tree, (2 * n), o_c[node], -query[2])
