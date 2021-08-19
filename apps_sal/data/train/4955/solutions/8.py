from numpy import product


def ride(group, comet):

    def alph_pos(l):
        return ord(l) - 64

    def compute_score(name):
        return product([alph_pos(c) for c in name]) % 47
    group_score = compute_score(group)
    comet_score = compute_score(comet)
    return 'GO' if group_score == comet_score else 'STAY'
