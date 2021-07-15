def dna_to_rna(dna):
    result =  ""
    for i in dna:
        if i == "T":
            result +='U'
        else:
            result+=i
    return result

