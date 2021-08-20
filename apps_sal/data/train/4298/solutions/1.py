import re
reg = (("[.',]", ''), ('too?', '2'), ('fore?', '4'), ('oo', '00'), ('be', 'b'), ('are', 'r'), ('you', 'u'), ('please', 'plz'), ('people', 'ppl'), ('really', 'rly'), ('have', 'haz'), ('know', 'no'), ('s', 'z'))


def n00bify(stg):
    (caps, lol) = (stg[0] in 'hH', stg[0] in 'wW')
    words = ['LOL'] if lol else []
    for w in stg.split():
        first = w[0].isupper()
        for (p, r) in reg:
            w = re.sub(p, r, w, flags=re.I)
        words.append(f'{w[0].upper()}{w[1:]}' if first else w)
    if len(re.sub('[?!]', '', ' '.join(words))) > 31:
        words.insert(lol, 'OMG')
    (num, out) = (len(words), ' '.join((w if i % 2 else w.upper() for (i, w) in enumerate(words, 1))))
    out = re.sub('([?!])', '\\1' * num, out).replace('!!', '!1')
    return out.upper() if caps else out
