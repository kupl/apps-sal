from numpy import matrix


def lucasnum(n):
    return int((matrix('2 1; 1 3') * matrix('0 1; 1 1' if n >= 0 else '-1 1; 1 0', object) ** abs(n))[0, 0])
