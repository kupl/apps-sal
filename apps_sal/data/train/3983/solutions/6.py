def Xbonacci(signature, n):
    length = len(signature)
    for i in range(n - len(signature)):
        signature.append(sum(signature[-length:]))
    return signature[:n]
