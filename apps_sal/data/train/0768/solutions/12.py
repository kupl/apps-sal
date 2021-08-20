import sys
(input, print) = (sys.stdin.readline, sys.stdout.write)
sys.setrecursionlimit(10 ** 6)


def ans(dic, n):
    if dic.get(n) != None:
        b = []
        for a in dic[n]:
            b.append(ans(dic, a))
        mx = 0
        node = 0
        for a in b:
            if a[0] > mx:
                mx = a[0]
            node += a[1]
        node += len(dic[n])
        return (mx + node + 1, node)
    else:
        return (1, 0)


for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    dic = {}
    for j in range(1, n):
        temp = a[j - 1]
        if dic.get(temp) == None:
            dic[temp] = [j + 1]
        else:
            dic[temp].append(j + 1)
    anss = ans(dic, 1)
    print(str(anss[0]) + '\n')
