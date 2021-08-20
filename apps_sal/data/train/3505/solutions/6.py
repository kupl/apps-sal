def super_pad(string, width, fill=' '):
    if width == 0:
        return ''
    diff = width - len(string)
    f = fill
    if diff >= 0:
        if len(f) > 0 and f[0] in ['<', '^', '>']:
            if f[0] == '<':
                f = fill[1:]
                return (f * width)[:width - len(string)] + string
            elif f[0] == '^':
                f = fill[1:]
                a = (width - len(string)) // 2
                b = width - len(string) - a
                return (f * width)[:b] + string + (f * width)[:a]
            elif f[0] == '>':
                f = fill[1:]
                return string + (f * width)[:width - len(string)]
        else:
            return (f * width)[:width - len(string)] + string
    elif f[0] == '<':
        f = fill[1:]
        return string[len(string) - width:]
    elif f[0] == '^':
        f = fill[1:]
        a = abs(width - len(string)) // 2
        b = abs(width - len(string)) - a
        return string[:a] + string[:-b]
    elif f[0] == '>':
        f = fill[1:]
        return string[:width - len(string)]
    else:
        return string[len(string) - width:]
