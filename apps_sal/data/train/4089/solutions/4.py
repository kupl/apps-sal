seq = []


def sum_dif_rev(n):
    i = seq[-1] if seq else 0
    while len(seq) < n:
        i += 9
        r = int(str(i)[::-1])
        if i % 10 and r != i and (r + i) % abs(r - i) == 0:
            seq.append(i)
    return seq[n - 1]
