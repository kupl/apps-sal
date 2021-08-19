def how_many_bees(hive):
    if hive is None or len(hive) == 0:
        return 0
    cnt = 0
    for row in hive:
        cnt += ''.join(row).count('bee')
        cnt += ''.join(row).count('eeb')
    (m, n) = (len(hive), len(hive[0]))
    cols = [''.join([hive[j][i] for j in range(m)]) for i in range(n)]
    cnt += sum([i.count('bee') for i in cols])
    cnt += sum([i.count('eeb') for i in cols])
    return cnt
