def indices(n, d):

    result = ([i] for i in range(d + 1))  # start with all possible lists of length 1 with sum within limit

    # until have lists of len n: add every possible num to each list in result that doesn't put over limit d
    for iteration in range(n - 1):
        result = (i + [j] for i in result for j in range(d + 1) if sum(i) + j <= d)

    return list(filter(lambda r: sum(r) == d, result))  # return combinations with sum d
