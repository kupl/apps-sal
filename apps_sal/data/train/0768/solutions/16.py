import sys

sys.setrecursionlimit(10**6)


def recurse(root):
    if root not in dic:
        return (1, 1)
    sum1 = 1
    max1 = 0
    for i in dic[root]:
        x, y = recurse(i)
        sum1 += x
        max1 = max(max1, y)
    return sum1, sum1 + max1


for _ in range(int(input())):
    n = int(input())

    dic = {}
    lis = list(map(int, input().split()))
    for i in range(len(lis)):
        if lis[i] not in dic:
            dic[lis[i]] = [i + 2]
        else:
            dic[lis[i]].append(i + 2)
    x, y = recurse(1)
    print(y)
