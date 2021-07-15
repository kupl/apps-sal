def poly_multiply(p1, p2):
    ans = [0] * (len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            ans[i + j] += p1[i] * p2[j]
    return any(ans) and ans or []
