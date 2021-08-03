def is_haiku(s, v='aeiouy'):
    C = []
    for x in [a.strip('.;:!?,').split()for a in s.lower().split('\n')]:
        t = ''
        for y in x:
            if y.endswith('e') and any(c in y[:-1]for c in v):
                y = y[:-1]
            for c in y:
                t += c if c in v else' 'if t and t[-1] != ' 'else''
            t += ' '
        C += [len(t.split())]
    return C == [5, 7, 5]
