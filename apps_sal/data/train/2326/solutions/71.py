import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    A = [int(a) for a in input().split()]
    nDict = dict()
    Atype = list(set(A))
    Atype.sort(reverse=True)
    Atype.append(0)
    for i, a in enumerate(A):
        if a in nDict:
            nDict[a].append(i)
        else:
            nDict[a] = [i]
    count = [0] * N
    minIndex = N
    group = 0
    for i in range(len(Atype) - 1):
        cN = Atype[i]
        minIndex = min(minIndex, nDict[cN][0])
        group += len(nDict[cN])
        nextN = Atype[i + 1]
        count[minIndex] += (cN - nextN) * group
    print("\n".join(map(str, count)))

    return 0


def __starting_point():
    solve()


__starting_point()
