def encode(st):
    L = []
    A = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}
    for i in st:
        if i in A:
            L.append(A[i])
        else:
            L.append(i)
    return "".join(L)


def decode(st):
    L = []
    A = {"1": "a", "2": "e", "3": "i", "4": "o", "5": "u"}
    for i in st:
        if i in A:
            L.append(A[i])
        else:
            L.append(i)
    return "".join(L)
