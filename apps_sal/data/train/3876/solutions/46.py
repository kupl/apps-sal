def find(n):
    total = 0
    testCase = 1
    while testCase <= n:
        if testCase % 3 == 0 or testCase % 5 == 0:
            total += testCase
        testCase += 1
    return total
