def player_manager(players):
    return [{'player': p.strip(), 'contact': int(c)} for p, c in zip(players.split(',')[::2], players.split(',')[1::2])] if players else []
