def draw(waves):
    mx = max(waves)
    return '\n'.join((''.join(c) for c in zip(*[(mx - w) * '□' + w * '■' for w in waves])))
