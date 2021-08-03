D = {'bumpy': {'red': '0.57', 'yellow': '0.28', 'green': '0.14'}, 'smooth': {'red': '0.33', 'yellow': '0.33', 'green': '0.33'}}

# That's a weird kata, only 6 possibles results and no randomness


def color_probability(color, texture):
    return D[texture][color]
