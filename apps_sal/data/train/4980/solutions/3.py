SEP = ';'


def sort_csv_columns(csv):
    names = csv.split('\n', 1)[0].lower().split(SEP)
    d = {names.index(c): i for (i, c) in enumerate(sorted(names))}
    return '\n'.join((SEP.join((e[1] for e in sorted([(d[i], field) for (i, field) in enumerate(row.split(SEP))]))) for row in csv.split('\n')))
