def color_probability(color, texture):
    prob_mapper = {'smooth': {
        'red': 1,
        'yellow': 1,
        'green': 1,
        'total': 3
    }, 'bumpy': {
        'red': 4,
        'yellow': 2,
        'green': 1,
        'total': 7
    }}

    prob = prob_mapper[texture][color] / prob_mapper[texture]['total']

    return str(prob)[:4]
