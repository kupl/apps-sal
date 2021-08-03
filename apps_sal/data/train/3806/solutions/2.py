def black_and_white(h, w, compressed):
    s = ''.join('BW'[i % 2] * b for i, b in enumerate(compressed))
    r = [s[i:i + w].replace('WB', 'W B').replace('BW', 'B W') for i in range(0, h * w, w)]
    r = [([0] if row[0] == 'W' else []) + [len(w) for w in row.split()] for row in r]
    return [e + ([0] if len(e) % 2 else []) for e in r]
