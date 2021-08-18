def Xbonacci(signature, n):
    seq = signature[:n]
    for i in range(n - len(signature)):
        seq.append(sum(seq[-len(signature):]))
    return seq
