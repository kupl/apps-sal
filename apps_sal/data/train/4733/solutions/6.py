def rot_energies(B, Jmin, Jmax):
    return [] if B <= 0 else [B * I * (I + 1) for I in range(Jmin, Jmax + 1)]
