def E(B, J):
    return B*J*(J+1)
    
def rot_energies(B, Jmin, Jmax):
    if B < 0 or Jmax < Jmin: return []
    return [E(B, j) for j in range(Jmin, Jmax+1)]

