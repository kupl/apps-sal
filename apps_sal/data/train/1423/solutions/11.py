testCases = int(input())
for time in range(1, testCases + 1):
    length = int(input())
    numList = [int(item) for item in input().split()]
    k = int(input())
    mark = numList[k - 1]
    numList.sort()
    print(numList.index(mark) + 1)
