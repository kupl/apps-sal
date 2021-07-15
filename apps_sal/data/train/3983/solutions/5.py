def Xbonacci(signature, n):
    result = []
    for i in range(n):
        signature.append(sum(signature))
        result.append(signature.pop(0))
    return result
