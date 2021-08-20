import re
(NEG, DOT, _, *DIGS) = '负点 零一二三四五六七八九'
POWS = ' 十 百 千 万'.split(' ')
NUMS = {str(i): c for (i, c) in enumerate(DIGS)}
for n in range(10):
    NUMS[str(n + 10)] = POWS[1] + DIGS[n] * bool(n)


def to_chinese_numeral(n):
    ss = str(abs(n)).split('.')
    return NEG * (n < 0) + parse(ss[0]) + (len(ss) > 1 and decimals(ss[1]) or '')


def decimals(digs):
    return DOT + ''.join((NUMS[d] for d in digs))


def parse(s):
    if s in NUMS:
        return NUMS[s]
    s = ''.join(reversed([NUMS[d] + POWS[i] * (d != '0') for (i, d) in enumerate(reversed(s))]))
    return re.sub(f'零+$|(?<=零)零+', '', s)
