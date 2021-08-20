PROBS = [[1, 1, 1], [4, 2, 1]]
IDX = {'red': 0, 'yellow': 1, 'green': 2, 'smooth': 0, 'bumpy': 1}


def color_probability(color, texture):
    prob = PROBS[IDX[texture]][IDX[color]] / sum(PROBS[IDX[texture]])
    return '{:.2}'.format(int(prob * 100) / 100)
