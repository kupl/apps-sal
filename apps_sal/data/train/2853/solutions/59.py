def solve(arr):
    a = []
    for i in arr[::-1]:
        if (i in a) == False:
            a.append(i)
    return a[::-1]
