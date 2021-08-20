def learn_charitable_game(a_list):
    if not any(a_list):
        return False
    elif sum(a_list) % len(a_list):
        return False
    return True
