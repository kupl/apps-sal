def html(xn, *args, **kwargs):
    props = ''.join((' ' + ('class' if p == 'cls' else p) + '="' + kwargs[p] + '"' for p in kwargs))
    return '\n'.join((f'<{xn}{props}>{v}</{xn}>' for v in args)) if args else f'<{xn}{props} />'
