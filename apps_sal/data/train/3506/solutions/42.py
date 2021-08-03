def vowel_indices(w):
    return [i + 1 for i, c in enumerate(w) if c in "aeiouyAEIOUY"]
