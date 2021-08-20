def spin_solve(sentence):
    r = []
    for s in sentence.split():
        (p, c) = (s.endswith('.'), s.endswith(','))
        s = s[:-1] if p or c else s
        if len(s) > 6 or s.lower().count('t') > 1:
            r.append(s[::-1] + ('.' if p else ',' if c else ''))
        elif len(s) == 2 or c:
            r.append(s.upper() + ('.' if p else ',' if c else ''))
        elif len(s) == 1:
            r.append('0' + ('.' if p else ',' if c else ''))
        else:
            r.append(s + ('.' if p else ',' if c else ''))
    return ' '.join(r)
