from collections import defaultdict


def sort_csv_columns(s):
    d = defaultdict(list)
    for i in s.splitlines():
        for (j, k) in enumerate(i.split(';')):
            d[j].append(k)
    r = zip(*[i[1] for i in sorted(d.items(), key=lambda x: (x[1][0].lower(), x[1][0]))])
    return '\n'.join([';'.join(i) for i in r])
