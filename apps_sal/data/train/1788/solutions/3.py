# function to calculate whether everything is lost or not
def xor_all(game_state):
    result = 0
    for pile in game_state:
        result ^= pile
    return result


def choose_move(game_state):
    game_state_copy = list(game_state)
    # remove duplicate values (do not waste time on them, later on)
    for i, val in enumerate(game_state_copy):
        if val and game_state_copy.count(val) > 1:
            game_state_copy[i] = 0
            game_state_copy[game_state_copy.index(val)] = 0
    if xor_all(game_state):
        # check for each pile, whether it is possible to check apropriate number of piles
        for i, pile in enumerate(game_state_copy):
            # try with every possible number of straws
            for straws in range(0, pile+1):
                if xor_all(game_state_copy[:i] + [straws] + game_state_copy[i+1:]) == 0:
                    return [i, pile-straws]
    print "I have lost"
    return [0, 0]
