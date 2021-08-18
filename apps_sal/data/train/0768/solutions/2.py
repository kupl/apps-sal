
from sys import setrecursionlimit
setrecursionlimit(10**8)


def max_mex(dept):

    for i in at_dept[dept]:

        m, l = 0, 0
        for j in child[i]:
            m = max(m, mex[j][1])
            l += mex[j][0]

        mex[i] = [l + 1, m + l + 1]

    if(dept > 1):
        max_mex(dept - 1)


def all_dept(arr, dept=2):
    for i in arr:
        at_dept[dept].append(i)
        all_dept(child[i], dept + 1)


for T in range(int(input())):
    n = int(input())
    parent = list(map(int, input().split()))

    child = [[] for i in range(n + 1)]
    for i in range(n - 1):

        child[parent[i]].append(i + 2)

    at_dept = [[] for i in range(n + 1)]
    at_dept[1].append(1)
    all_dept(child[1])

    for arr in at_dept[::-1]:
        if(arr == []):
            at_dept.pop()
        else:
            break

    mex = [0] * (n + 1)
    for i in at_dept[-1]:
        mex[i] = [1, 1]

    max_mex(len(at_dept) - 2)

    print(mex[1][1])
