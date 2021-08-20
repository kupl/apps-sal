def motif_locator(s, motif):
    return [i + 1 for (i, c) in enumerate(s) if s[i:i + len(motif)] == motif]
