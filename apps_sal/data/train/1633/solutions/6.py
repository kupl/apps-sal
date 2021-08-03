import re
import math
numerals = {
    "-": "负",
    ".": "点",
    0: "零",
    1: "一",
    2: "二",
    3: "三",
    4: "四",
    5: "五",
    6: "六",
    7: "七",
    8: "八",
    9: "九",
    10: "十",
    100: "百",
    1000: "千",
    10000: "万"
}


def decimal(n):
    out = []
    for x in list(n):
        out.append(numerals[int(x)])
    return ''.join(out)


def to_chinese_numeral(n):
    c, bla = divmod(n, 10)
    a, shi = divmod(c, 10)
    b, bai = divmod(a, 10)
    wan, qian = divmod(b, 10)
    if n == 0:
        return numerals[0]
    if n < 0:
        return numerals['-'] + to_chinese_numeral(-n)

    if isinstance(n, float):
        b = ''.join(re.findall('[\.][0-9]+', str(n)))[1:]
        return to_chinese_numeral(int(''.join(re.findall('[0-9]+[\.]', str(n)))[:-1])) + numerals['.'] + decimal(b)
    a = [wan, 10000, qian, 1000, bai, 100, shi, 10, bla]

    b = ''.join(numerals[x] for x in a)
    out = re.sub('[零]*$', '', b)
    out = re.sub('[零]{2,}', '零', out)
    out = re.sub('零.', '零', out)
    out = re.sub('[零]{2,}', '零', out)
    out = re.sub('^零', '', out)
    out = re.sub('^一十', '十', out)
    out = re.sub('[零]*$', '', out)
    return out
