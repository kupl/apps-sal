def hamster_me(k, s):
    return ''.join(map({c: w[0] + str(n) for w in __import__('re').findall('.[^%s]*' % k, ''.join(map(chr, range(97, 123))) * 2) for (n, c) in enumerate(w, 1)}.get, s))
