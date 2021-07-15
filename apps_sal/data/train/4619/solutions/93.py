whoseMove = lambda last_player, win: ('black', 'white', 'black')[('black', 'white').index(last_player) + (not win)]
