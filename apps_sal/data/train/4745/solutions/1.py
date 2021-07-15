def group_groceries(groceries):
    categories = { 'fruit':[], 'meat':[], 'other':[], 'vegetable':[] }
    for product in groceries.split(','):
        key, value = product.split('_')
        categories[key if key in categories else 'other'].append(value)
    return '\n'.join('{}:{}'.format(cat, ','.join(sorted(items))) for cat, items in categories.items())
