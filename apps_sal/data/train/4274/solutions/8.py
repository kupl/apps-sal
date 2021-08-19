from itertools import repeat
import operator
import math
import re


def do_math(s):
    (final, official) = ([int(i[1]) for i in sorted([[re.search('[A-Za-z]', i).group(), ''.join(re.findall('\\d', i))] for i in s.split()], key=lambda x: x[0])], ['+', '-', '*', '/'])
    (d, temp, c) = ({'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}, sum(repeat(official, math.ceil(len(final) / 4)), []), final[0])
    for i in range(1, len(temp[:len(final)])):
        c = d[temp[i - 1]](c, final[i])
    return round(c)
