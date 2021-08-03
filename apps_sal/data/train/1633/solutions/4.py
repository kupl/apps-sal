from itertools import starmap

numerals = {
    "-": "负",
    ".": "点",
    '0': "零",
    '1': "一",
    '2': "二",
    '3': "三",
    '4': "四",
    '5': "五",
    '6': "六",
    '7': "七",
    '8': "八",
    '9': "九",
    1: "",
    2: "十",
    3: "百",
    4: "千",
    5: "万"
}


def helper(i, s):
    if i:
        return ''.join(map(numerals.get, s))
    l, res = len(s), []
    for j, c in enumerate(s):
        if c == '0':
            if i or not (res and res[-1] == numerals[c]):
                res.append(numerals[c])
        else:
            if j or c != '1' or l != 2:
                res.append(numerals[c])
            res.append(numerals[l - j])
    if res[0] != res[-1] == numerals['0']:
        del res[-1]
    return ''.join(res)


def to_chinese_numeral(n):
    x, s = '', str(n)
    if s[0] == '-':
        x, s = numerals['-'], s[1:]
    return x + numerals['.'].join(starmap(helper, enumerate(s.split('.'))))
