def Xbonacci(signature,n):
    size = len(signature)
    while len(signature) < n:
        signature.append(sum(signature[-size:]))
    return signature[:n]
