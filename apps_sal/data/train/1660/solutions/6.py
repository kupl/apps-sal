from collections import defaultdict
import re
def simplify(poly):
    terms = defaultdict(lambda: 0)
    for a, b, c in re.findall(r'([+-]?)(\d*?)([a-z]+)', poly):
        terms[''.join(sorted(c))] += eval(a + (b or '1'))
    return (
        re.sub
        (
            r'((?<=[-+])|\b)1(?=[a-z])|((?:[-+])|\b)0(?:[a-z]+)|\+(?=-)',
            '',
            '+'.join([f'{terms[x]}{x}' for x in sorted(list(terms.keys()), key = lambda x: (len(x), x))])
        )
    )

