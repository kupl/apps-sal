def diamond(n):
    if n % 2 == 0 or n <= 0:                        # validate input
        return None
    diamond = ""                                 # initialize diamond string
    for i in range(n):                            # loop diamond section lines
        length = getLength(i, n)                  # get length of diamond section
        diamond += getLine(length, n)             # generate diamond line
    return diamond


def getLine(len, max):
    spaces = (max - len) // 2                         # compute number of leading spaces
    return (" " * spaces) + ("*" * len) + "\n"    # create line


def getLength(index, max):
    distance = abs(max // 2 - index)                # find distance from center (max length)
    return max - distance * 2                       # compute length of diamond section
