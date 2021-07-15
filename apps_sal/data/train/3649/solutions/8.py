def aa_percentage(sequence,list = ["A", "I", "L", "M", "F", "W", "Y", "V"]):
    counts = [sequence.count(x) for x in list]
    return round(sum(counts)*100/len(sequence),0)
