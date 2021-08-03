def Xbonacci(signature, n):
    l = len(signature)
    for i in range(n - l):
        signature.append(sum(signature[-l:]))
    return signature[:n]
