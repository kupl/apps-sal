def group_groceries(groceries):
    groups = ['fruit', 'meat', 'other', 'vegetable']
    d = {}
    for item in groceries.split(','):
        (g, i) = item.split('_')
        g = g if g in groups else 'other'
        try:
            d[g].append(i)
        except:
            d[g] = [i]
    final_string = []
    for g in groups:
        try:
            group_string = g + ':' + ','.join(sorted(d[g]))
        except:
            group_string = g + ':'
        final_string.append(group_string)
    return '\n'.join(final_string)
