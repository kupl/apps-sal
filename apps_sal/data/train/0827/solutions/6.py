tulu = int(input())
for _ in range(tulu):
    n, k = [int(x) for x in input().split()]
    data = input()
    counterA = 0
    counterB = 0
    indexListOfA = []
    indexListOfB = []
    for i in range(n):
        if(data[i] == 'a'):
            counterA += 1
            indexListOfA.append(i)
        if(data[i] == 'b'):
            counterB += 1
            indexListOfB.append(i)
    sumOfOneData = 0
    for j in indexListOfA:
        lenB = len(indexListOfB)
        if(lenB == 0):
            break
        flag = False
        while len(indexListOfB) > 0 and flag == False:
            if(j < indexListOfB[0]):
                sumOfOneData += len(indexListOfB)
                flag = True
            else:
                indexListOfB.pop(0)
    lulu = (k * (k - 1)) // 2
    result = lulu * counterB * counterA + k * sumOfOneData
    print(result)
