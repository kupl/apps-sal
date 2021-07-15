def rot_energies(B, Jmin, Jmax):
    if B<=0:
        return []
    return [B * J * (J + 1) for J in range(Jmin,Jmax+1)]
