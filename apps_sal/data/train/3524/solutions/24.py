def dna_to_rna(dna):
    RNA = ''
    for letter in dna:
        if letter == 'T':
            RNA += 'U'
        else:
            RNA += letter
    return RNA
