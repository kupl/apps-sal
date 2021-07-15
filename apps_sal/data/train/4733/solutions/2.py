def rot_energies(B, Jmin, Jmax):
    return [B * j * (j + 1) for j in range(Jmin, Jmax + 1)] if B > 0 else []
