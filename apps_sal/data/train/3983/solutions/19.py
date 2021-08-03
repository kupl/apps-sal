def Xbonacci(signature, n):
    x = len(signature)
    for i in range(n - x):
        signature.append(sum(signature[-x:]))
    arr = signature[:n]
    return arr
