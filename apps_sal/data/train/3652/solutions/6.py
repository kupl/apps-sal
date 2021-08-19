def button_sequences(R, B):
    return (lambda r, f: r.sub('(.)\\1+', '\\1', f.reduce(lambda x, y: x + ('_' if y == ('0', '0') else 'R' if y == ('1', '0') else 'B' if y == ('0', '1') else 'R' if x[-1:] in ['', '_', 'R'] else 'B'), zip(R, B), '')).replace('_', ''))(__import__('re'), __import__('functools'))
