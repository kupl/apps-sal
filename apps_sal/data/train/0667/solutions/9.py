def getAns(d, arr):
    latestDate = 0
    tempToMatch = d
    for ele in arr:
        latestDate = ele * (tempToMatch // ele)
        tempToMatch = latestDate
    return latestDate


def __starting_point():
    t = int(input())
    for _ in range(t):
        (N, D) = input().split()
        Arr = list(map(int, input().strip().split()))
        print(getAns(int(D), Arr[::-1]))


__starting_point()
