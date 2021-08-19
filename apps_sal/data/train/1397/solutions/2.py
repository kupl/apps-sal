def findM(A, n):
    elemIdxMap = dict()
    for i in range(n):
        if A[i] in elemIdxMap:
            elemIdxMap[A[i]].append(i)
        else:
            elemIdxMap[A[i]] = [i]
    keys = sorted(elemIdxMap.keys())
    connected = False
    count = 0
    prevIdx = -1
    nKeys = len(keys)
    for i in range(nKeys - 1):
        if not connected:
            prevIdx = elemIdxMap[keys[i]][0]
            for idx in elemIdxMap[keys[i + 1]]:
                if idx > prevIdx:
                    connected = True
                    count += 1
                    prevIdx = idx
                    break
        else:
            connected = False
            for idx in elemIdxMap[keys[i + 1]]:
                if idx > prevIdx:
                    connected = True
                    count += 1
                    prevIdx = idx
                    break
    return nKeys - count


def __starting_point():
    for _ in range(int(input())):
        n = int(input())
        A = list(map(int, input().split()))
        print(findM(A, n))


__starting_point()
