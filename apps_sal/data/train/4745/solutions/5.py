def group_groceries(groce):
    box = {'fruit': [], 'meat': [], 'other': [], 'vegetable': []}
    groce = [e.split('_') for e in groce.split(',')]
    for k, v in groce:
        box.get(k, box['other']).append(v)
    return '\n'.join(f'{k}:{",".join(sorted(v))}' for k, v in box.items())
