from collections import Counter


def neigthboors(peaks):
    for x, y in peaks:
        yield x, y - 1
        yield x - 1, y
        yield x, y
        yield x + 1, y
        yield x, y + 1


def peak_height(mountain):
    mountain = [(x, y) for y, row in enumerate(mountain) for x, p in enumerate(row) if p == "^"]
    i = 0
    while mountain:
        mountain = [x_y for x_y, cnt in list(Counter(neigthboors(mountain)).items()) if cnt == 5]
        i += 1
    return i
