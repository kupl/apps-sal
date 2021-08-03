D = {w: (len([c for c in w if c in 'aeiou']), len([c for c in w if c not in 'aeiou'])) for w in WORD_LIST}


def wanted_words(n, m, forbid_let):
    return [w for w in WORD_LIST if D[w] == (n, m) and not [c for c in forbid_let if c in w]]
