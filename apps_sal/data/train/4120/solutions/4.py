def sort_dict(d):
    'return a sorted list of tuples from the dictionary'
    #items = list(d.items())
    return sorted(list(d.items()), key=lambda i: -i[1])
