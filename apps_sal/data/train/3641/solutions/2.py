def reverse_complement(dna):
    base_pair ={'A':'T','T':'A','C':'G','G':'C'}
    return "".join(base_pair[base] for base in dna[::-1].upper()) if set(dna.upper()).issubset({'A','T','C','G',""})  else "Invalid sequence"
