tulu = int(input())
for _ in range(tulu):
    n, k = [int(x) for x in input().split()]
    data = input()
    counterA = 0
    counterB = 0
    sumOfOneData = 0
    indexListOfB = []
    for i in range(n):
        if(data[i] == 'a'):
            counterA += 1
        if(data[i] == 'b'):
            counterB += 1
            sumOfOneData += counterA
    lulu = (k * (k - 1)) // 2
    result = (lulu * counterB * counterA) + (k * sumOfOneData)
    print(result)
