def aa_percentage(seq, residues=["A", "I", "L", "M", "F", "W", "Y", "V"]):
    return round(sum(seq.count(r) for r in residues) / len(seq) * 100)
