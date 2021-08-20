for tests in range(int(input())):
    n = int(input())
    blockHeights = [int(blockHeight) for blockHeight in input().split()]
    sumOfBlockHeightsBefore = sum(blockHeights)
    blockHeights[0] = blockHeights[n - 1] = 1
    for i in range(1, n):
        if blockHeights[i] > blockHeights[i - 1] + 1:
            blockHeights[i] = blockHeights[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if blockHeights[i] > blockHeights[i + 1] + 1:
            blockHeights[i] = blockHeights[i + 1] + 1
    heightOfTallestTemple = max(blockHeights)
    s = heightOfTallestTemple ** 2
    noOfOperations = sumOfBlockHeightsBefore - s
    print(noOfOperations)
