def merged(p, q):
    pc = 0
    qc = 0
    ra = []
    while True:
        if pc < len(p) and qc < len(q):
            if p[pc] < q[qc]:
                ra.append(p[pc])
                pc = pc + 1
            else:
                ra.append(q[qc])
                qc = qc + 1
        elif pc < len(p):
            ra.append(p[pc])
            pc = pc + 1
        elif qc < len(q):
            ra.append(q[qc])
            qc = qc + 1
        else:
            break
    return ra


def mysort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        part1 = mysort(arr[:mid])
        part2 = mysort(arr[mid:])
        return merged(part1, part2)


def nth_smallest(arr, pos):
    arr = mysort(arr)
    return arr[pos - 1]
