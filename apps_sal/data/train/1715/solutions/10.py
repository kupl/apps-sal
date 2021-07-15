def iterate_over_lines(text, width):
    i, lim = 0, len(text) - width
    while i < lim:
        j = text.rfind(' ', i, i + width + 1)
        yield text[i: j]
        i = j + 1
    yield text[i:]
    
def justify_line(line, width):
    words = line.split()
    if len(words) < 2:
        return line
    ch = sum(len(w) for w in words)
    d, m = divmod(width - ch, len(words) - 1)
    gaps = [' ' * (d + int(i < m)) for i in range(len(words) - 1)] + ['']
    parts = [part for t in zip(words, gaps) for part in t]
    return ''.join(parts)

def justify(text, width):
    lines = list(iterate_over_lines(text, width))
    lines = [justify_line(s, width) for s in lines[: -1]] + [lines[-1]]
    return '\n'.join(lines)

