def solve(arr):
    l = []
    n = 0
    for x in arr:
        for y in range(1, len(x) + 1):
            if y == ord(x[y - 1].lower()) - 96:
                n += 1
        l.append(n)
        n = 0
    return l
