import re

colors = dict.fromkeys('0123456789', 'orange')
colors.update(F='pink', L='red', R='green')

def repl(m):
    c = m.group()
    return '<span style="color: {}">{}</span>'.format(colors[c[:1]], c)
    
def highlight(code):
    return re.sub('F+|L+|R+|[0-9]+', repl, code)
