import re


def vowel_indices(word):
    iter = re.finditer('[aeiouy]', word.lower())
    indices = [m.start(0) + 1 for m in iter]
    return indices
