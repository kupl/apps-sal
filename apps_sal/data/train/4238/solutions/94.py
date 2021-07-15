def squares_needed(grains):
    chess = []
    rice = 1
    for i in range(1,65):
        chess.append(rice)
        rice *= 2
    return max([chess.index(i) for i in chess if grains >= i])+1 if grains else 0
