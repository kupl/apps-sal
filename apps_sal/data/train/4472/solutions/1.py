def bear_fur(bears):
    return {('black', 'black'): 'black', ('black', 'white'): 'grey', ('black', 'brown'): 'dark brown', ('brown', 'brown'): 'brown', ('brown', 'white'): 'light brown', ('white', 'white'): 'white'}.get(tuple(sorted(bears)), 'unknown')
