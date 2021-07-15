def rot_energies(B, Jmin, Jmax):
    return [] if B < 0 or Jmin > Jmax else [B * i * (i + 1) for i in range(Jmin, Jmax + 1)]
