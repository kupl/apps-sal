def player_manager(players):
    if not players:
        return []
    players = players.split(", ")
    return [{"player": player, "contact": int(contact)} for player, contact in zip(players[::2], players[1::2])]
