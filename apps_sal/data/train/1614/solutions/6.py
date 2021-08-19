def who_is_winner(moves):
    G = {(c, r): ' ' for r in range(6) for c in range(7)}
    for (col, colour) in [(ord(m[0]) - ord('A'), m[2]) for m in moves]:
        for row in range(6):
            if G[col, row] == ' ':
                G[col, row] = colour
                break
        if colour * 4 in ' '.join([''.join((G[col, k] for k in range(6))), ''.join((G[k, row] for k in range(7))), ''.join((G.get((k, row - col + k), ' ') for k in range(7))), ''.join((G.get((k, row + col - k), ' ') for k in range(7)))]):
            return {'Y': 'Yellow', 'R': 'Red'}[colour]
    return 'Draw'
