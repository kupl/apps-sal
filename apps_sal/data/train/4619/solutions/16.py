def whoseMove(last_player: str, win: bool) -> str:
    """ Get info whose turn is on the next round based on given last player's move and his result. """
    return ['white', 'black'][any([all([last_player == 'black', win is True]), all([last_player == 'white', win is False])])]
