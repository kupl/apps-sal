def gc_content(seq):
    return bool(seq) and round(100 * (seq.count('C') + seq.count('G')) / len(seq), 2)
