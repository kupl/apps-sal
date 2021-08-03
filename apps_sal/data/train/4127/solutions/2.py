TOP = 20000
CNT = [1] * TOP
for i in range(2, TOP):
    for j in range(i, TOP, i):
        CNT[j] += 1


def count_pairs_int(diff, n_max):
    return sum(CNT[a] == CNT[a + diff] for a in range(1, n_max - diff))
