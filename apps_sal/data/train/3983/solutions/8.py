def Xbonacci(signature, n):
    length = len(signature)
    [signature.append(sum(signature[-length:])) for i in range(length, n)]
    return signature[:n]
