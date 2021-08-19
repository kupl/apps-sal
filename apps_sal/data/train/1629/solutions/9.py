def exchange_sort(sequence):
    print(sequence)
    # Reduce the sequence into its useful data
    counts = [sequence.count(n) for n in [7, 8, 9]]
    dividers = [0] + [sum(counts[:i]) for i in range(1, 4)]
    groupings = [[sequence[dividers[i]:dividers[i + 1]].count(n) for n in [7, 8, 9]] for i in range(3)]
    # Perform swaps en masse until done
    n = 0

    def swap(t0, t1, n0, n1):
        swappable = min(groupings[t0][n1], groupings[t1][n0])
        groupings[t0][n0] += swappable
        groupings[t0][n1] -= swappable
        groupings[t1][n1] += swappable
        groupings[t1][n0] -= swappable
        return swappable
    for a, b in [(0, 1), (0, 2), (1, 2)]:
        n += swap(a, b, a, b)
    for a, b, c in [(0, 1, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0), (1, 0, 2), (0, 2, 1)]:
        n += swap(a, b, a, c)
    for a, b in [(0, 1), (0, 2), (1, 2)]:
        n += swap(a, b, a, b)
    return n
