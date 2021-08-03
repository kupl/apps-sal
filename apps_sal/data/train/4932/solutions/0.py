def find_solution(m):
    return [j for j, r in enumerate(m) if r[0] ^ m[0][0]] + [len(m) + i for i, b in enumerate(m[0]) if not b]
