def aa_percentage(seq, targets=["A", "I", "L", "M", "F", "W", "Y", "V"]):
    return round(sum([seq.count(ch) for ch in targets])/len(seq)*100)
