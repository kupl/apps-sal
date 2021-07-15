# For learning purposes. From slowest to fastest.
#
# s9n = avg(sorted(timeit.Timer("seven_ate90('6797974797977979797979797979797979733262',)", this_file).repeat(10, 1000)))
# Averages:
# s90 = 0.00537808943730594922
# s91 = 0.00240899947496580821

import re

REGEXP = re.compile(r'79(?=7)')

def seven_ate9(str_):
    return REGEXP.sub('7', str_)

def seven_ate9(str_):
    while '797' in str_:
        str_ = str_.replace('797', '77')
    return str_
