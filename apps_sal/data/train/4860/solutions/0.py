def amidakuji(ar):
    numbers = list(range(len(ar[0]) + 1))
    for line in ar:
        for (i, swap) in enumerate(line):
            if swap == '1':
                (numbers[i], numbers[i + 1]) = (numbers[i + 1], numbers[i])
    return numbers
