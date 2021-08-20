def gc_content(seq):
    return round(100 * sum((x in 'GC' for x in seq)) / (len(seq) or 1), 2)
