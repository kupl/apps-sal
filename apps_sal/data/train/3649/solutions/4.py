def aa_percentage(seq, codes=['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    return round(100 * len([x for x in seq if x in codes]) / len(seq))
