import re


def motif_locator(sequence, motif):
    return [m.start() + 1 for m in re.finditer('{}(?={})'.format(motif[0], motif[1:]), sequence)]
