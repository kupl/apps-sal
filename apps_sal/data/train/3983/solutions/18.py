def Xbonacci(signature,n):
    sequence = signature[:]
    for i in range(len(signature), n):
        sequence.append(sum(sequence[i-len(signature):i]))
    return sequence[:n]
