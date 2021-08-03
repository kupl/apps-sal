def tribonacci(signature, n):
    s = signature.copy()
    while len(s) < n:
        s.append(sum(s[-3:]))
    return s[:n]
