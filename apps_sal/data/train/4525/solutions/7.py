def check_challenge(p, c, m):
    if p == c:
        return 'Challenge is completed.'
    n = 'an eb ar pr ay un ul ug ep ct ov ec'.split().index(m[1:3])
    s = p // 12 * n + min(p % 12, n) - c
    return 'You are ' + ('%s schedule' % ('%d ahead of' % -s, '%d behind' % s)[0 < s] + '.!'[s < 0], 'on track.')[n == 0 or s == 0]
