def mysterious_pattern(m, n):
    if m == 1:
        return('o')
    
    seq = [1, 1]
    for i in range(m - 2): # Generate fibonacci sequence
        seq.append(seq[-2]+seq[-1])

    for i, v in enumerate(seq): 
        seq[i] = v % n

    pattern = []
    for i in range(max(seq)+1):
        pattern.append([])

    for x in seq: # Add 'o' and ' ' at the right places
        for j, row in enumerate(pattern):
            if x == j:
                pattern[j].append('o')
            else:
                pattern[j].append(' ')

    for i in range(min(seq)): # Remove empty rows
        del pattern[i]

    res = ''
    for row in pattern:
        res += ''.join(row).rstrip() + '\n'

    return(res[:-1])

