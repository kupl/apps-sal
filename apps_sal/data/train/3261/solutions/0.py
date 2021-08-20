import re
from collections import OrderedDict
scale = '2 3 4 5 6 7 8 9 10 J Q K A'.split(' ')


def sort_poker(john, uncle):
    order = list(OrderedDict.fromkeys(re.findall('([SDHC])[0-9JQKA]+', uncle)))
    john = re.findall('([SDHC])([0-9JQKA]+)', john)
    return ''.join((''.join(i) for i in sorted(john, key=lambda x: (order.index(x[0]), scale.index(x[1])))))
