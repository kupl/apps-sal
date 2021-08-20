t = int(input())
for unused in range(t):
    n = int(input())
    minA = 200
    minB = 200
    for used in range(n):
        inputString = input()
        countA = 0
        countB = 0
        for i in inputString:
            if i == 'a':
                countA += 1
            else:
                countB += 1
        if countA < minA:
            minA = countA
        if countB < minB:
            minB = countB
    print(min(minA, minB))
