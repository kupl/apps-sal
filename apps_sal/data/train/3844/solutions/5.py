def poly_multiply(p1, p2):
    answer = [0] * (len(p1) + len(p2) - 1)
    for i, coeff1 in enumerate(p1):
        for j, coeff2 in enumerate(p2):
            answer[i + j] += coeff1 * coeff2
    return [] if all(coeff == 0 for coeff in answer) else answer

def poly_from_roots(r):
    if not r:
        return [1]
    parts = [[-root, 1] for root in r]
    answer = parts[0]
    for part in parts[1:]:
        answer = poly_multiply(answer, part)
    return answer
