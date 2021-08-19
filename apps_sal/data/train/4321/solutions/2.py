def player_manager(players):
    if not players:
        return []
    lst = players.split(', ')
    return [{'player': name, 'contact': int(num)} for (name, num) in zip(lst[::2], lst[1::2])]
