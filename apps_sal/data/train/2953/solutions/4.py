from collections import defaultdict


def numericals(s):
    temp = []
    a = defaultdict(int)

    for i in s:
        a[i] = a[i] + 1
        temp.append(a[i])

    return ''.join(map(str, temp))
