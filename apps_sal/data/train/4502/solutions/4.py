def tribonacci(signature, n):
    output = signature[:n]
    while len(output) < n:
        output.append(sum(output[-3:]))
    return output
