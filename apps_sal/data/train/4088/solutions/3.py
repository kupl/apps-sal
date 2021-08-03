from collections import Counter


def tetris(arr):
    fields = Counter()
    clear = 0
    for log in arr:
        pos = log[1:].replace('R0', 'L0')
        fields[pos] += int(log[0])
        if fields[pos] >= 30:
            break
        elif len(fields) == 9:
            c = min(fields.values())
            clear += c
            for pos in fields:
                fields[pos] -= c
    return clear
