def base_finder(seq):
    base = 0
    for i in range(10):
        number = seq[i]
        for i in range(len(number)):
            if int(number[i]) > base:
                base = int(number[i])
    return base + 1
