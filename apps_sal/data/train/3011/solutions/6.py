def learn_charitable_game(a):
    t = sum(a) / len(a)
    return t != 0 and t.is_integer()
