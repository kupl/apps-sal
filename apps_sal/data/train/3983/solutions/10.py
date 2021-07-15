def Xbonacci(sequence, n):
    i = 0
    while len(sequence) < n:
        sequence.append(sum(sequence[i:]))
        i+=1
    return sequence[:n]
