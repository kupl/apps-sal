def count_targets(n, seq):
    count = 0
    for i in range(n, len(seq)):
        if seq[i] == seq[i - n]:
            count += 1
    return count
