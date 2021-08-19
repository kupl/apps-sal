def get_required(player, enemy):
    (s1, s2) = (sum(player), sum(enemy))
    return 'Auto-win' if s1 >= s2 + 6 else 'Auto-lose' if s2 >= s1 + 6 else 'Random' if s1 == s2 else 'Pray for a tie!' if s1 + 5 == s2 else f'(1..{5 + s1 - s2})' if s1 < s2 else f'({7 - s1 + s2}..6)'
