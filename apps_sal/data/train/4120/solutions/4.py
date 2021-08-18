def sort_dict(d):
    'return a sorted list of tuples from the dictionary'
    return sorted(list(d.items()), key=lambda i: -i[1])
