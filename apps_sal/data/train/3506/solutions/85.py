L = 'aeiouyAEIOUY'
vowel_indices = lambda s: [i + 1 for i, c in enumerate(s) if c in L]
