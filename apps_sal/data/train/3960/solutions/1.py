def align_right(text, width):
    res = []
    line = []
    for word in text.split():
        if len(' '.join(line + [word])) <= width:
            line.append(word)
        else:
            res.append(line)
            line = [word]
    res.append(line)
    return '\n'.join((' '.join(line).rjust(width) for line in res))
