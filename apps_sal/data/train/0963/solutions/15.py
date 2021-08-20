for _ in range(0, int(input())):
    N = int(input())
    count = 0
    hillsH = list(map(int, input().split()))

    def FindAns(hills):
        maxIndex = 0
        maxNum = max(hills)
        maxIndex = hills.index(maxNum)
        listRight = []
        listLeft = []
        if maxIndex == 0 or maxIndex == len(hills) - 1:
            return 1
        for i in range(0, maxIndex):
            listLeft.append(hills[i])
        for i in range(maxIndex + 1, len(hills)):
            listRight.append(hills[i])
        return 1 + min(FindAns(listLeft), FindAns(listRight))
    print(FindAns(hillsH))
