reverse_complement = lambda s, d="ACGT": s.translate(str.maketrans(d, "TGCA"))[::-1]if set(s) <= set(d)else"Invalid sequence"
