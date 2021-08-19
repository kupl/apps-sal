def player_manager(players):
    result = []
    if not players:
        return []
    players = players.split(', ')
    for (i, x) in enumerate(players):
        if i % 2 == 0:
            result.append({})
            result[-1]['player'] = x
        else:
            result[-1]['contact'] = int(x)
    return result
