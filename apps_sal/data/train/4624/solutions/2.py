def gc_content(seq):
    return round(sum(c in 'GC' for c in seq) / len(seq) * 100, 2) if len(seq) else 0.0
