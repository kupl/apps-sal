def dna_to_rna(dna):
    result = []
    for i in dna:
        if i == "T":
            result.append("U")
        else:
            result.append(i)
    return ''.join(result)
