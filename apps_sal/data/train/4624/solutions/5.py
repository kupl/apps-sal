def gc_content(seq):
    return round(100 * (seq.count('G') + seq.count('C')) / len(seq), 2) if seq else 0
