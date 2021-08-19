def bear_fur(bears):
    combos = {('black', 'brown'): 'dark brown', ('black', 'white'): 'grey', ('brown', 'white'): 'light brown'}
    if bears[0] == bears[1]:
        return bears[0]
    else:
        colors = tuple(sorted(bears))
        if colors in combos:
            return combos[colors]
        else:
            return 'unknown'
