pos = {'L4': 0, 'L3': 1, 'L2': 2, 'L1': 3, 'L0': 4, 'R0': 4, 'R1': 5, 'R2': 6, 'R3': 7, 'R4': 8}


def tetris(arr):
    (current, res) = ([0] * 9, 0)
    for x in arr:
        p = pos[x[1:]]
        current[p] += int(x[0])
        if current[p] >= 30:
            break
        y = min(current)
        if y:
            (current, res) = ([v - y for v in current], res + y)
    return res
