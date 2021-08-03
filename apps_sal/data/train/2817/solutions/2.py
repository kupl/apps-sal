def DNA_strand(dna):
    reference = {"A": "T",
                 "T": "A",
                 "C": "G",
                 "G": "C"
                 }
    return "".join([reference[x] for x in dna])
