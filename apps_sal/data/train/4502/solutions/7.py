def tribonacci(signature,n):
    [signature.append(sum(signature[i-3:i])) for i in range(3,n)]
    return signature[0:n]
