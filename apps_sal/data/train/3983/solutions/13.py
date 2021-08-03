def Xbonacci(signature, n):
    x = len(signature)
    for _ in range(n - x):
        signature.append(sum(signature[-x:]))
    return signature[:n]
