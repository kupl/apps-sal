def gc_content(seq):
    return 0.0 if not seq else round((seq.count('G') + seq.count('C')) / float(len(seq)) * 100, 2)
