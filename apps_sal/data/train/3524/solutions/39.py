def dna_to_rna(dna):
    answer = ""
    for letter in dna:
        if letter == "T":
            answer += "U"
        else:
            answer += letter
    return answer
