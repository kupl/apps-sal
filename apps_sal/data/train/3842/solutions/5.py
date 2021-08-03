def word_wrap(text, limit):
    wraped = []
    line = ''
    for w in text.split():
        while len(line) <= limit and len(w) > limit:
            split = max(0, limit - len(line) - bool(line))
            if split > 0:
                line += ' ' * bool(line) + w[:split]
            wraped.append(line)
            line = ''
            w = w[split:]
        if len(line) + len(w) + bool(line) <= limit:
            line += ' ' * bool(line) + w
        else:
            wraped.append(line)
            line = w
    if line or w:
        wraped.append(line or w)
    return '\n'.join(wraped)
