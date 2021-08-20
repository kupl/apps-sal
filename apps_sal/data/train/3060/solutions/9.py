def get_required(player, enemy):
    (p, e) = (sum(player), sum(enemy))
    math_wins = [x for x in range(1, 7) if p + x > e + 6]
    lucky = [x for x in range(1, 7) if e + x < p + 6]
    return 'Random' if p == e else 'Auto-win' if p >= e + 6 else 'Auto-lose' if e >= p + 6 else 'Pray for a tie!' if e - p == 5 else '({}..{})'.format(min(math_wins), max(math_wins)) if p > e else '({}..{})'.format(min(lucky), max(lucky))
