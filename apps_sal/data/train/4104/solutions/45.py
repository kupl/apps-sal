def merge(a, b):
    ac = 0
    bc = 0
    ra = []
    while True:
        if ac < len(a) and bc < len(b):
            if a[ac] > b[bc]:
                ra.append(a[ac])
                ac = ac + 1
            else:
                ra.append(b[bc])
                bc = bc + 1
        elif ac < len(a):
            ra.append(a[ac])
            ac = ac + 1
        elif bc < len(b):
            ra.append(b[bc])
            bc = bc + 1
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
        return merge(part1, part2)


def max_tri_sum(numbers):
    nodup = {}
    for x in numbers:
        nodup[x] = 0
    nodup = list(nodup.keys())
    nodup = mysort(nodup)
    i = 0
    s = 0
    while i < 3:
        s = s + nodup[i]
        i = i + 1
    return s
