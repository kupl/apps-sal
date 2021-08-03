def digits(num):
    ints = [int(i) for i in str(num)]
    sums = []
    for i in range(len(ints) - 1):
        for j in ints[i + 1:]:
            sums.append(ints[i] + j)
    return sums
