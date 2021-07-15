def whoseMove(last_player, win):
    other = 'black' if last_player == 'white' else 'white'
    return last_player if win else other
