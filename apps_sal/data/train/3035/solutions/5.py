def getMatrixProduct(a, b):
    return -1 if len(list(zip(*a))) != len(b) else [[sum((k * l for (k, l) in zip(i, j))) for j in zip(*b)] for i in a]
