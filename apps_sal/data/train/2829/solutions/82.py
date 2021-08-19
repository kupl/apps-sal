def array_madness(a, b):
    squareSum = 0
    cubeSum = 0
    for i in a:
        squareSum += i * i
    for i in b:
        cubeSum += i * i * i
    if squareSum > cubeSum:
        return True
    return False
