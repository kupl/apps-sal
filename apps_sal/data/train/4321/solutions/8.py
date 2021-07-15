def player_manager(players):
    if not players: return []
    p = players.split(', ')
    return [{'player': p[i], 'contact': int(p[i + 1])} for i in range(0, len(p) - 1, 2)]
