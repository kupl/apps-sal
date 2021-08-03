def find_longest(arr):
    length = []
    for i, v in enumerate(arr):
        length.append([len(str(v)), i])

    multiple = []
    for z in length:
        if z[0] == sorted(length)[-1][0]:
            multiple.append(z)

    return arr[multiple[0][1]]
