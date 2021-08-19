def solve(n):
    (l, seq) = ([1], [i for i in range(2, n + 1)])
    while l[-1] <= len(seq):
        l.append(seq.pop(0))
        del seq[l[-1] - 1::l[-1]]
    return sum(l + seq)
