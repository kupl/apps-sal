def backwardsPrime(start, stop):
    output = []
    for x in range(start, stop + 1):
        if isPrime(x):
            if isReversePrime(x):
                output.append(x)
    return output


def isPrime(input):
    if input % 2 == 0:
        return False
    for x in range(3, int(input ** 0.5) + 1, 2):
        if input % x == 0:
            return False
    else:
        return True


def isReversePrime(input):
    tempstr = ''
    iptemp = str(input)
    i = len(iptemp) - 1
    while i >= 0:
        tempstr += iptemp[i]
        i = i - 1
    temp = 0
    temp = int(tempstr)
    if input == temp:
        return False
    if isPrime(temp):
        return True
    else:
        return False
