def rot_energies(B, Jmin, Jmax):
    result = []
    if B >= 0:
        for a in range(Jmin, Jmax + 1):
            result.append(B * a * (a + 1))
    return result
