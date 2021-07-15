def player_manager(players):
    return [{'player': a, 'contact': int(b)} for a, b in zip(*[iter(players.split(', '))] * 2)] if players else []
