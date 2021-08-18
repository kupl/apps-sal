from operator import itemgetter


def next_smaller(n):
    s = str(n)
    LR_Pairs = list(enumerate(zip(s, s[1:])))
    iP, pivot = next(((i, l) for i, (l, r) in reversed(LR_Pairs) if l > r), (-1, -1))
    if iP == -1:
        return -1

    iM, mx = max(((i, c) for i, c in enumerate(s[iP + 1:], iP + 1) if c < pivot), key=itemgetter(1))
    nextS = s[:iP] + mx + ''.join(sorted(s[iP:iM] + s[iM + 1:], reverse=True))

    return int(nextS) if nextS[0] != '0' else -1
