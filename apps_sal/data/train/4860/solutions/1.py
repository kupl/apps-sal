def amidakuji(ar):
    width = len(ar[0])
    current = [i for i in range(width + 1)]
    for i in ar:
        layer = i
        count = 0
        for s in layer:
            if s == "1":
                current = swap(current, count, count + 1)
            count += 1
    return current


def swap(l, pos1, pos2):
    l[pos1], l[pos2] = l[pos2], l[pos1]
    return l
