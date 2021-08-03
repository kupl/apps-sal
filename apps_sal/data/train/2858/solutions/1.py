def combs(comb1, comb2):
    options = []
    for i in range(max(len(comb1), len(comb2)) + 1):
        if ('*', '*') not in zip(' ' * i + comb1, comb2):
            options.append(max(len(comb1) + i, len(comb2)))
        if ('*', '*') not in zip(comb1, ' ' * i + comb2):
            options.append(max(len(comb1), len(comb2) + i))
    return min(options)
