def inside_out(s):
    return ' '.join(w[:m][::-1] + w[m] * (L % 2) + w[-m:][::-1] * (L > 1)
                    if w else w
                    for w, m, L in map(lambda w: (w, len(w) // 2, len(w)), s.split(' ')))
