from collections import deque
(N, M) = list(map(int, input().split()))
adjL = [set(range(N)) for _ in range(N)]
for v in range(N):
    adjL[v].remove(v)
for _ in range(M):
    (A, B) = list(map(int, input().split()))
    (A, B) = (A - 1, B - 1)
    adjL[A].remove(B)
    adjL[B].remove(A)


def getSizes(adjList):

    def bfs(vSt):
        colors[vSt] = 1
        nums[1] += 1
        Q = deque([vSt])
        while Q:
            vNow = Q.popleft()
            color = colors[vNow]
            for v2 in adjList[vNow]:
                if colors[v2] == color:
                    return False
                elif colors[v2] == 0:
                    colors[v2] = -color
                    nums[-color] += 1
                    Q.append(v2)
        return True
    numV = len(adjList)
    colors = [0] * numV
    anss = []
    for vSt in range(numV):
        if colors[vSt] != 0:
            continue
        nums = {-1: 0, 1: 0}
        if not bfs(vSt):
            return []
        anss.append((nums[-1], nums[1]))
    return anss


sizes = getSizes(adjL)
if not sizes:
    print(-1)
else:
    bitset = 1 << N
    for (A, B) in sizes:
        bitset = bitset >> A | bitset >> B
    minDiff = N
    iMinDiff = -1
    for i in reversed(list(range(N + 1))):
        if bitset & 1:
            diff = abs(i - N / 2)
            if diff < minDiff:
                minDiff = diff
                iMinDiff = i
        bitset >>= 1
    print(iMinDiff * (iMinDiff - 1) // 2 + (N - iMinDiff) * (N - iMinDiff - 1) // 2)
