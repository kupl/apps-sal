import re


def decompose_single_strand(single_strand):
    return '\n'.join(('Frame {}: {}'.format(i, ' '.join((m.group() for m in re.finditer(r, single_strand)))) for (i, r) in enumerate(['...', '^.|...|..$', '^..|...|.$'], 1)))
