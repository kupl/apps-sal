def almost_increasing_sequence(seq):
    l = [i for i, (a, b) in enumerate(zip(seq[:-1], seq[1:])) if a >= b]
    return not l or len(l) == 1 and (l[0] == 0 or l[0] == len(seq) - 2 or seq[l[0] - 1] < seq[l[0] + 1] or seq[l[0]] < seq[l[0] + 2])
