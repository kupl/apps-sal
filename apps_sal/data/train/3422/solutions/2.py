def diamond(n):
    if n % 2 == 0 or n <= 0:
        return None
    diamond = ""
    for i in range(n):
        length = getLength(i, n)
        diamond += getLine(length, n)
    return diamond


def getLine(len, max):
    spaces = (max - len) // 2
    return (" " * spaces) + ("*" * len) + "\n"


def getLength(index, max):
    distance = abs(max // 2 - index)
    return max - distance * 2
