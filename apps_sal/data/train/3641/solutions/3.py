def reverse_complement(dna):
    reverse = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    r_c = ''
    for nucl in reversed(dna):
        if nucl not in reverse:
            return 'Invalid sequence'
        else:
            r_c += reverse[nucl]
    return r_c
