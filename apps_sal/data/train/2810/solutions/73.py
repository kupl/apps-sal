def solve(arr):
    narr = []
    for x in arr:
        i = 0
        for j in range(len(x)):
            if ord(x[j].lower()) - 97 == j:
                i += 1
        narr.append(i)
    return narr
