def color_probability(color, texture):
    marbles = {'smooth': {'red': 1, 'yellow': 1, 'green': 1, 'total': 3}, 'bumpy': {'red': 4, 'yellow': 2, 'green': 1, 'total': 7}}
    return '{}'.format(marbles[texture][color] / marbles[texture]['total'])[:4]
