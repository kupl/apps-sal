from numpy import prod


def find_spec_prod_part(n, com):
    partitions = []
    current_partition = 2
    while n > 1:
        if n % current_partition == 0:
            partitions.append(current_partition)
            n /= current_partition
            current_partition = 2
        else:
            current_partition += 1

    if len(partitions) == 1:
        return "It is a prime number"

    result = [([0], -1)] if com == "max" else [([0], float('Inf'),)]
    sc_opt(partitions, result, com)

    result[0][0].sort(reverse=True)
    return [result[0][0], result[0][1]]


def sc_opt(partitions, result, com):
    if (com == "min" and result[0][1] > sc(partitions)) or (com == "max" and result[0][1] < sc(partitions)):
        result[0] = (partitions, sc(partitions))
    if len(partitions) == 2 or (com == "min" and max(partitions) > result[0][1]) or (com == "min" and max(partitions) > result[0][1]):
        return
    for p in set(partitions):
        current = partitions.copy()
        current.remove(p)
        for i in filter(lambda x: x >= p, set(current)):
            curr = current.copy()
            curr[curr.index(i)] *= p
            sc_opt(curr, result, com)


def sc(partitions):
    return sum([p ** partitions.count(p) for p in set(partitions)]) * len(partitions)
