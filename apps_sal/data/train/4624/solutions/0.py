def gc_content(seq):
    if not seq:
        return 0.0
    else:
        res = seq.count('C') + seq.count('G')
        return round(res * 100 / len(seq), 2)
