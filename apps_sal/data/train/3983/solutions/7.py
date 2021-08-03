def Xbonacci(signature, n):
    sig = len(signature)
    if sig > n:
        return signature[:n]
    xbon = signature
    for i in range(sig, n):
        xbon.append(sum(xbon[i - sig:]))
    return xbon
