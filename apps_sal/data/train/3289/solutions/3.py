def motif_locator(s, motif):
    return [i + 1 for i in range(len(s) - len(motif) + 1) if s[i:].startswith(motif)]
