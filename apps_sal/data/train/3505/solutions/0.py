def super_pad(string, width, fill=" "):
    if fill.startswith('>'):
        return (string + width * fill[1:])[:width]
    elif fill.startswith('^'):
        pad = (width * fill[1:])[:max(0, width - len(string) + 1) // 2]
        return (pad + string + pad)[:width]
    else:
        if fill.startswith('<'): fill = fill[1:]
        return (width * fill)[:max(0, width - len(string))] + string[max(0, len(string) - width):]
