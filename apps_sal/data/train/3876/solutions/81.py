def find(n):
    finalSum = 0
    for i in range(n+1):
        if i % 3 == 0:
            finalSum += i
        elif i % 5 == 0:
            finalSum += i
    return finalSum
