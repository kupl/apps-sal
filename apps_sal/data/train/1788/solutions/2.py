def choose_move(game_state):
    nim = reduce(lambda x,y: x ^ y, game_state, 0)
    return [(i, x - (x ^ nim)) for i,x in enumerate(game_state) if x ^ nim < x][0]
