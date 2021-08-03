def bestMovie():
    tests = int(input())
    for t in range(tests):
        n = int(input())
        L = list(map(int, input().split()))
        R = list(map(int, input().split()))
        maxIndex = -1
        maxValue = 0
        for i in range(n):
            prod = L[i] * R[i]
            if maxValue < prod:
                maxValue = prod
                maxIndex = i
            elif maxValue == prod:
                if R[maxIndex] < R[i]:
                    maxIndex = i
        print(maxIndex + 1)


bestMovie()
