def solve(arr):
    l = []
    for i in arr:
        a = 0
        i = i.lower()
        for ii in range(len(i)):
            if ii == ord(i[ii]) - 97:
                a += 1
        l.append(a)
    return l
