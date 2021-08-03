def tribonacci(signature, n):
    return signature[:n] if n <= len(signature) else tribonacci(signature + [sum(signature[-3:])], n)
