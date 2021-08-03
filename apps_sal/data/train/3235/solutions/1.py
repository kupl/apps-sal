def decompose_single_strand(single_strand):
    f1 = 'Frame 1: {}'.format(decompose(single_strand))
    f2 = 'Frame 2: {} {}'.format(single_strand[:1], decompose(single_strand[1:]))
    f3 = 'Frame 3: {} {}'.format(single_strand[:2], decompose(single_strand[2:]))
    return '\n'.join([f1, f2, f3])


def decompose(strand):
    return ' '.join([strand[i: i + 3] for i in range(0, len(strand), 3)])
