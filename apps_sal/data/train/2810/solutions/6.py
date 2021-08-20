def solve(arr):
    a = [x.lower() for x in arr]
    b = []
    for x in a:
        aa = 0
        for i in range(len(x)):
            if ord(x[i]) - 96 == i + 1:
                aa = aa + 1
        b.append(aa)
    return b
