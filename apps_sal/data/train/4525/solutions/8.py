def check_challenge(p, c, m):
    if p == c:
        return'Challenge is completed.'
    n = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split().index(m[:3])
    s = p // 12 * n + min(p % 12, n) - c
    return"You are " + ("%s schedule" % ('%d ahead of' % (-s), '%d behind' % s)[0 < s] + '.!'[s < 0], "on track.")[n == 0 or s == 0]
