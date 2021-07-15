def distinct(seq):
    """return list of distnct values maintaining list order"""
    return [ seq[i] for i in range(len(seq)) if seq[i] not in seq[:i] ]

