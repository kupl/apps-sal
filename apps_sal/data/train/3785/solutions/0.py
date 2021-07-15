def generate_diagonal(d, l):
    result = [1] if l else []
    for k in range(1, l):
        result.append(result[-1] * (d+k) // k)
    return result
