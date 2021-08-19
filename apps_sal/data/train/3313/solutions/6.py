import re


def highlight(code):
    colors = dict(zip('FLR0123456789', ['pink', 'red', 'green'] + ['orange'] * 10))
    span = '<span style="color: {}">{}</span>'
    regex = '(F+|L+|R+|[0-9]+|\\(|\\))'

    def highlight_command(g):
        return g if g in '()' else span.format(colors[g[:1]], g)
    return ''.join((highlight_command(m.group(0)) for m in re.finditer(regex, code)))
