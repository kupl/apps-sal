def get_required(player, enemy):
    p, e = sum(player), sum(enemy)
    return 'Random' if p == e else\
           'Auto-win' if p >= e + 6 else\
           'Auto-lose' if e >= p + 6 else\
           'Pray for a tie!' if e - p == 5 else\
           '({}..6)'.format(e + 7 - p) if p > e else\
           '(1..{})'.format(p + 6 - e - 1)
