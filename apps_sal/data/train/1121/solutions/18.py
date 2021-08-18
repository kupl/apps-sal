testcases = int(input())
while testcases != 0:
    testcases -= 1
    n = input()
    hr = int(n[0:2]) % 12
    minte = int(n[3:])
    degree = .5 * (60 * hr - 11 * minte)

    if degree.is_integer():
        degree = int(degree)

    degree = abs(degree)
    if degree > 180:
        degree = 360 - degree
    print(str(degree) + " degree")
