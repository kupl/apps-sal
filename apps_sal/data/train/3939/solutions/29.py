def rps(p1: str, p2: str) -> str:
    """ Get information which player won! In case of a draw return Draw! """
    score_rules = {'scissors': {'paper': True, 'rock': False}, 'paper': {'scissors': False, 'rock': True}, 'rock': {'scissors': True, 'paper': False}}
    if p1 == p2:
        return 'Draw!'
    elif score_rules.get(p1).get(p2):
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'
