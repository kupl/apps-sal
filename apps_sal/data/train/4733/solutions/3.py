def rot_energies(B, Jmin, Jmax):
    return [B * J * (J + 1) for J in range(Jmin, Jmax + 1)] * (B > 0)
