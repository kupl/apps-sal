def Guess_it(N, M):
    def mass(g, r, b): return (g * 5) + (r * 4) + (b * 3)
    results = []
    for g in range(N + 1):
        for r in range((N - g) + 1):
            b = N - r - g
            if mass(g, r, b) == M:
                results.append([g, r, b])
    return results
