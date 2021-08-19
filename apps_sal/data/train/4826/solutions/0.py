import re
from collections import Counter
from itertools import chain
p = re.compile('{legs}{body}{body}0{body}{body}0{body}{body}{legs}'.format(legs='[a-z]', body='[[\\]|};&#/><()*]'))


def count_robots(a):
    cnt = Counter(chain.from_iterable((['d' if 'mechanik' in line else 'w' if 'automatik' in line else ''] * len(p.findall(line)) for line in map(str.lower, a))))
    return ['{w} robots functioning automatik'.format_map(cnt), '{d} robots dancing mechanik'.format_map(cnt)]
