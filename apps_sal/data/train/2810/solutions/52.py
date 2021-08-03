def solve(arr):
    l = []
    for i in arr:
        c = 0
        for j in range(0, len(i)):
            if j + 1 == ord(i[j].lower()) - 96:
                c += 1
        l.append(c)
    return l
