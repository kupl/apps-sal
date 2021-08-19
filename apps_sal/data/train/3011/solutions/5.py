def learn_charitable_game(a_list):
    if not any(a_list):
        # no positive values
        return False
    elif sum(a_list) % len(a_list):
        # not an integer start
        return False
    return True
