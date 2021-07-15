def rps(p1, p2):
    return f"Player {1+(p1[0]+p2[0] in 'psrp')} won!" if p1 != p2 else 'Draw!'
