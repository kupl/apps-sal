def check_challenge(p, c, m, M='Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()):
    if p == c:
        return'Challenge is completed.'
    D = [0] * 12
    while p:
        for i, x in enumerate(D):
            if p == 0:
                break
            D[i] += 1
            p -= 1
    m = M.index(m[:3])
    s = sum(D[:m]) - c
    if m == 0 or s == 0:
        return "You are on track."
    return "You are %s schedule" % ('%d behind' % s if 0 < s else '%d ahead of' % (-s)) + '.!'[s < 0]
