def Xbonacci(signature,n):
    l = len(signature)

    for i in range(l, n):
        signature += [sum(signature[i-l:i])]
    return signature[:n]
