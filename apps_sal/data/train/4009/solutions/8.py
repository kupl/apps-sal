def digits_average(input):
    l = [int(list(str(input))[i]) for i in range(len(str(input)))]
    while len(l) != 1:
        l = [(l[i] + l[i + 1]) // 2 + (l[i] + l[i + 1]) % 2 for i in range(len(l) - 1)]
    return l[0]
