def complete_binary_tree(a):

    def in_order(n=0):
        if n < len(a):
            yield from in_order(2 * n + 1)
            yield n
            yield from in_order(2 * n + 2)
    result = [None] * len(a)
    for (i, x) in zip(in_order(), a):
        result[i] = x
    return result
