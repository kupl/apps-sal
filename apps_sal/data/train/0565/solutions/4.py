def binarySearch(start, end, xindex, opList):
    if start <= end:
        midindex = int((start + end) / 2)

        opList.append(midindex)
        if xindex < midindex:
            return binarySearch(start, midindex - 1, xindex, opList)

        elif xindex > midindex:
            return binarySearch(midindex + 1, end, xindex, opList)

        else:
            return opList


def counter(opList, a, x):
    small = 0
    big = 0
    rightSmall = 0
    rightBig = 0

    for i in range(len(opList) - 1):
        # print("for oplist[",i,"]=",opList[i])
        if opList[i] < opList[i + 1]:
            # print("traverse to right")
            if x < a[opList[i]]:
                # print("x is small")
                small += 1
            else:
                rightSmall += 1
        else:
            # print("traverse to left")
            if x > a[opList[i]]:
                # print("x is big")
                big += 1
            else:
                rightBig += 1
    flag = isBigSmallAvailable(small, big, x, a, rightBig, rightSmall)
    if flag:
        total = small + big
        total = total - min(small, big)
        return total
    else:
        return -1


def isBigSmallAvailable(small, big, x, a, rightBig, rightSmall):
    s = 0
    b = 0
    length = len(a)
    for i in range(length):
        if a[i] < x:
            s += 1
        if a[i] > x:
            b += 1
    s = s - rightSmall
    b = b - rightBig
    # print("big ",b)
    if s >= small and b >= big:
        return True
    return False


t = int(input())
swapCount = 0
swaped = []
visited = []
for z in range(t):
    l = list(map(int, input().split()))
    n = int(l[0])
    q = int(l[1])
    aa = list(map(int, input().split()))
    for i in range(q):
        swapCount = 0
        swaped.clear()
        visited.clear()
        a = aa[:]
        # print("aa is",aa)

        x = int(input())
        # a.sort()
        xindex = a.index(x)
        opList = []
        result = binarySearch(0, n - 1, xindex, opList)
        count = counter(opList, a, x)

        # print(result)
        print(count)
        # else:
        #     print(swapCount)
