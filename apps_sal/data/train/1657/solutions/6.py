import copy


def string_func(s, x):
    m, l, arr, z = 0, len(s), [0] * len(s), 0
    while True:
        m += 1
        y = (2**m) % (2 * l + 1)
        if y == 1 or y == 2 * l:
            break
    for i in range(1, l, 2):
        arr[z] = i
        z += 1
    for i in range(l - 2 + l % 2, -1, -2):
        arr[z] = i
        z += 1
    ss = list(s)
    x %= m
    while x > 0:
        x -= 1
        for i in range(len(arr)):
            ss[arr[i]] = s[i]
        s = ss.copy()
    return ''.join(s)
