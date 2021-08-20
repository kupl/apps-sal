def align_right(text, width):
    k = text.split()
    out = ''
    last = []
    for x in k:
        if len(x + out) <= width:
            out += x + ' '
        else:
            last.append(out)
            out = x + ' '
    last.append(out)
    return '\n'.join((' ' * (width - len(x.rstrip())) + x.rstrip() for x in last))
