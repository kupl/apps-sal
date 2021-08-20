3
size = int(input())
num = list(map(int, input().split()))
rem = reversed(list(map(lambda x: int(x) - 1, input().split())))
chunks = [None] * size
res = [-1] * size
ans = [0] * size
ms = -1


def addChunk(n):
    chunks[n] = [n, num[n]]
    return n


def getRoot(n):
    while chunks[n][0] != n:
        n = chunks[n][0]
    return n


def mergeChunks(parent, child):
    proot = getRoot(parent)
    croot = getRoot(child)
    chunks[croot][0] = proot
    chunks[proot][1] += chunks[croot][1]
    return proot


for i in rem:
    res[i] = num[i]
    root = addChunk(i)
    if i > 0 and chunks[i - 1] != None:
        root = mergeChunks(i - 1, i)
    if i + 1 < size and chunks[i + 1] != None:
        root = mergeChunks(i, i + 1)
    ms = max(ms, chunks[root][1])
    ans.append(ms)
for i in range(1, size):
    print(ans[-i - 1])
print(0)
