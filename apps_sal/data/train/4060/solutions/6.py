def ant_bridge(ants, terrain):
    b = 0
    for i, c in enumerate(terrain):
        if c == '.':
            b += 1
        elif b:        
            b = b + (1 if terrain[i-2-b] == '.' else 2)
            ants, b = ants[-b:] + ants[:-b], 0

    return ants
