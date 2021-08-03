def sort_string(a, b):
    li = list(filter(lambda x: x in b, a))
    return ''.join(sorted(li, key=b.index) + [i for i in a if i not in li])
