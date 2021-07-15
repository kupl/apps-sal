def decipher_message(m):
    Q = int(len(m)**.5)
    return ''.join(''.join(i) for i in (zip(*[m[i:i+Q] for i in range(0, len(m), Q)]))) if m else ''
