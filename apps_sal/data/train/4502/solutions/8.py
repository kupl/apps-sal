def tribonacci(signature, n):
    for _ in range(3, n):
        signature += [sum(signature[-3:])]
    return signature[0:n]
