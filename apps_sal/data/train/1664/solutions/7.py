def amazon_check_mate(king, amazon):
    ranks = '87654321'
    fyles = 'abcdefgh'

    am = (ranks.index(amazon[1]), fyles.index(amazon[0]))
    ki = (ranks.index(king[1]), fyles.index(king[0]))

    amazon_attacks = set()
    knight_moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    for dr, dc in knight_moves:
        row, col = am[0] + dr, am[1] + dc
        if 0 <= row <= 7 and 0 <= col <= 7:
            amazon_attacks.add((row, col))

    rays = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dr, dc in rays:
        for d in range(1, 8):
            row, col = am[0] + d * dr, am[1] + d * dc
            if not (0 <= row <= 7) or not (0 <= col <= 7):
                break
            amazon_attacks.add((row, col))
            if (row, col) == ki:
                break

    king_attacks = set()
    for dr, dc in rays:
        row, col = ki[0] + dr, ki[1] + dc
        if 0 <= row <= 7 and 0 <= col <= 7:
            king_attacks.add((row, col))

    attacked = amazon_attacks | king_attacks

    def has_safe_move(r, c):
        for dr, dc in rays:
            row, col = r + dr, c + dc
            if (0 <= row <= 7 and 0 <= col <= 7) and (row, col) not in attacked:
                return True
        return False

    checkmates, checks, stalemates, safe = 0, 0, 0, 0
    for r in range(8):
        for c in range(8):
            if (r, c) in king_attacks or (r, c) == am or (r, c) == ki:
                continue
            if (r, c) in attacked:
                if has_safe_move(r, c):
                    checks += 1
                else:
                    checkmates += 1
            else:
                if has_safe_move(r, c):
                    safe += 1
                else:
                    stalemates += 1

    return [checkmates, checks, stalemates, safe]
