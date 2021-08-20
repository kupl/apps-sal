def draw(waves):
    m = max(waves)
    return '\n'.join((''.join(('□' if n < m - row else '■' for n in waves)) for row in range(m)))
