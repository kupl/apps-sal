CATEGORIES = ['fruit', 'meat', 'other', 'vegetable']
KNOWN = {c: c for c in CATEGORIES if c != 'other'}


def group_groceries(groceries):
    d = {key: [] for key in CATEGORIES}
    for item in groceries.split(','):
        (category, name) = item.split('_')
        d[KNOWN.get(category, 'other')].append(name)
    return '\n'.join((f"{c}:{','.join(sorted(d[c]))}" for c in CATEGORIES))
