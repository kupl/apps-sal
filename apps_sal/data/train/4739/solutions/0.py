D, R = {}, [[], [], []]
for i in range(10000):
    D[i] = D.get(i - 1, 0) + i
    R[D[i] % 3].append(D[i])


def same_col_seq(val, k, col):
    r = ['blue', 'red', 'yellow'].index(col)
    return [e for e in R[r] if e > val][:k]
