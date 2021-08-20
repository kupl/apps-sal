from re import sub


def repl(match):
    COLORS = {'F': 'pink', 'L': 'red', 'R': 'green'}
    match = match.group()
    color = COLORS.get(match[0], 'orange')
    return f'<span style="color: {color}">{match}</span>'


def highlight(code):
    return sub('F+|L+|R+|\\d+', repl, code)
