def get_required(player, enemy):
    p = player[0] + player[1]
    e = enemy[0] + enemy[1]
    if p == e:
        return 'Random'
    if p >= e + 6:
        return 'Auto-win'
    if e >= p + 6:
        return 'Auto-lose'
    if p > e:
        return '({0}..6)'.format(e - p + 7)
    if p + 5 > e:
        return '(1..{0})'.format(p - e + 5)
    return 'Pray for a tie!'
