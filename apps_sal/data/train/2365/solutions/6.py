from collections import defaultdict as dd
from pprint import pprint as pp


def solve():
    n = int(input())
    seqs = []
    d = dd(list)
    for _ in range(n - 1):
        seqs.append(list(map(int, input().split()[1:])))
    for seq in seqs:
        for i in range(len(seq)):
            s = ' '.join((str(x) for (j, x) in enumerate(seq) if j != i))
            d[s].append(seq[i])
    for st in range(1, n + 1):
        seq = [st]
        seq_set = {st}
        for _ in range(n - 1):
            found = False
            for l in range(len(seq)):
                k = ' '.join((str(x) for x in sorted(seq[-(l + 1):])))
                if k in d:
                    for j in d[k]:
                        if j not in seq_set:
                            seq.append(j)
                            seq_set.add(j)
                            found = True
                            break
                if found:
                    break
            if not found:
                break
        if len(seq) == n:
            print(' '.join((str(x) for x in seq)))
            break


for _ in range(int(input())):
    solve()
