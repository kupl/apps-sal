def group_groceries(groceries, categories='fruit meat other vegetable'.split()):
    groups = {category: [] for category in categories}
    for product in groceries.split(','):
        category, item = product.split('_')
        groups.get(category, groups['other']).append(item)
    return '\n'.join(f'{category}:{",".join(sorted(products))}'
                     for category, products in groups.items())
