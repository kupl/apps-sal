for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    (noOfPositive, noOfNegative, ans) = (0, 0, 0)
    for i in a:
        if i > 0:
            ans += i
            noOfPositive += 1
    ansList = []
    for i in range(noOfPositive):
        if a[i] <= 0:
            ansList.append(i + 1)
            noOfNegative += 1
    pList = []
    for i in range(n - 1, -1, -1):
        if noOfNegative == 0:
            break
        elif a[i] > 0:
            noOfNegative -= 1
            pList.append(i + 1)
    pList = reversed(pList)
    ansList += pList
    print(ans)
    print(len(ansList), *ansList)
