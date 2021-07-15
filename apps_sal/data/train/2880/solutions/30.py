def calc(currNum, steps):
    if (currNum <= 99):
        return (currNum, steps)
    
    y = currNum % 10
    x = (currNum - y)//10
    if (y == 0):
        return calc(x, steps + 1)

    nextNum = x - 2*y
    if (nextNum <= 99):
        return (nextNum, steps + 1)
    elif (nextNum >= 100):
        return calc(nextNum, steps + 1)

def seven(m):
    return calc(m, 0)

