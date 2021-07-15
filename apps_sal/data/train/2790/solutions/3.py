def dup(arr):
    a, res = 0, [x[0] for x in arr]
    for string in arr:
        for x in range(1, len(string)):
            if string[x] != string[x-1]:
                res[a] += string[x]
        a += 1
    return res
