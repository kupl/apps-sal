def combos(n):

    def partition(residue, acc):
        if residue == 0:
            yield acc[1:]
        else:
            for part in range(acc[-1], residue + 1):
                for result in partition(residue - part, acc + [part]):
                    yield result
    return list(partition(n, [1]))
