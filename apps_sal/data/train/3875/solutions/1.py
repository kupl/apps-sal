def draw(waves):
    m = max(waves)
    return '\n'.join((''.join(('□■'[x > i] for x in waves)) for i in reversed(range(m))))
