DEFAULT = 'unknown'
COLORS  = {'black'+'brown': 'dark brown',
           'black'+'white': 'grey',
           'brown'+'white': 'light brown'}

def bear_fur(bears):
    b1,b2 = sorted(bears)
    return b1 if b1==b2 else COLORS.get(b1+b2, DEFAULT)

