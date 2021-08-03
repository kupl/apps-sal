L = 'aeiouyAEIOUY'
def vowel_indices(s): return [i + 1 for i, c in enumerate(s) if c in L]
