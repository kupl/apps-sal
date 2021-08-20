def dna_to_rna(dna):
    output = []
    answer = ''
    for i in range(len(dna)):
        output += [dna[i]]
        if output[i] == 'T':
            output[i] = 'U'
        answer += output[i]
    return answer
