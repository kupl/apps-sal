import bisect
import sys
sys.setrecursionlimit(2147483647)

n = int(input())
a = list(map(int, input().split()))

tree = [[] for _ in range(n)]
for _ in range(n - 1):
    aa, bb = list(map(int, input().split()))
    tree[aa - 1].append(bb - 1)
    tree[bb - 1].append(aa - 1)

ans = [0] * n

# bisect.bisect_left(a, 4) #被ったら左側のindexを返す
# bisect.bisect_right(a, 4)#被ったら右側のindexを返す


def lisOnTree(x, lis):
    nonlocal ans, tree, a, n
    i = bisect.bisect_left(lis, a[x])
    if i == len(lis):
        lis.append(a[x])
        flag = "append"
    else:
        flag = (i, lis[i])
        lis[i] = a[x]
    # print(x,lis)
    ans[x] = len(lis)
    for item in tree[x]:
        if ans[item] == 0:
            lisOnTree(item, lis)
    if flag == "append":
        lis.pop()
    else:
        lis[flag[0]] = flag[1]


lisOnTree(0, [])

for item in ans:
    print(item)
