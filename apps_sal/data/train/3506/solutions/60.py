import re


def vowel_indices(word):
    return [k + 1 for k, l in enumerate(word) if bool(re.match('[aeuioy]', l, re.I))]
