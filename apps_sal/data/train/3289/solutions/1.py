def motif_locator(sequence, motif):
    return [i + 1 for (i, c) in enumerate(sequence) if sequence[i:i + len(motif)] == motif]
