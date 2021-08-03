sseq = [[1], [1, 1]]
s = [1, 1]
for t in range(2, 1800):
    s = [1] + [s[i - 1] + (i + 1) * s[i] for i in range(1, len(s))] + [1]
    sseq.append(s)


def combs_non_empty_boxesII(n):
    if n == 2:
        return [2, 1, 2]
    s = [1, 1]
    s = sseq[n - 1]
    return [sum(s), max(s), s.index(max(s)) + 1]
