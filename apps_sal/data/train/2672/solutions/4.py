def color_probability(color, texture):
    if texture == 'bumpy':
        if color == 'red':
            prob = 4 / 7
        elif color == 'yellow':
            prob = 2 / 7
        else:
            prob = 1 / 7
    else:
        prob = 1 / 3
    return str(prob)[:4]
