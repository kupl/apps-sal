import re


def repeating_fractions(numerator, denominator):
    ss = str(numerator / denominator).split('.')

    for x in range(0, 10):
        ss[1] = re.sub(r'[' + str(x) + r']{2,}', '(' + str(x) + ')', ss[1])

    return '.'.join(ss)
