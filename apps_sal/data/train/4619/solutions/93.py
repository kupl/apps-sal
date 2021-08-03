def whoseMove(last_player, win): return ('black', 'white', 'black')[('black', 'white').index(last_player) + (not win)]
