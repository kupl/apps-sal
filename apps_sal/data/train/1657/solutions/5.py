def exp(permutation, n):
    result = [-1] * len(permutation)
    for i in range(len(permutation)):
        if result[i] == -1:
            j, cycle = i, []
            while True:
                cycle.append(j)
                j = permutation[j]
                if i == j: break
            for j, k in enumerate(cycle):
                result[k] = cycle[(j + n) % len(cycle)]
    return result
    
def string_func(s, n):
    m = len(s)
    perm = [i // 2 if i % 2 else m - 1 - i // 2 for i in range(m)]
    return ''.join(s[i] for i in exp(perm, n))
