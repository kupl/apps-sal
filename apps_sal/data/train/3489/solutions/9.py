def save(sizes, hd):
    maxsize = 0
    copies = 0
    for i in range(len(sizes)):
        maxsize += sizes[i]
        copies += 1
        if maxsize > hd:
            return i
    return copies
