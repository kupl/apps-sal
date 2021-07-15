def seven(m):
    numSteps = 0
    while m >= 100:
        m = m // 10 - (m % 10) * 2
        numSteps += 1
    return (m, numSteps)
