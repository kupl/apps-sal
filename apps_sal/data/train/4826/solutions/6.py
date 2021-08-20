import re


def count_robots(a):
    d = {'automatik': 0, 'mechanik': 0}
    r = re.compile('[a-z](?:[|};&#\\[\\]\\/><()*]{2}0){2}[|};&#\\[\\]\\/><()*]{2}[a-z]')
    t = re.compile(f"\\b({'|'.join(d.keys())})\\b")
    for x in a:
        x = x.lower()
        (c, q) = (r.findall(x), t.search(x))
        if c and q:
            d[q.group()] += len(c)
    return [f'{v} robots {m} {k}' for ((k, v), m) in zip(d.items(), ('functioning', 'dancing'))]
