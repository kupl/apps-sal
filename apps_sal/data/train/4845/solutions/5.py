def sort_nested_list(A, emol=''):
    for e in str(A):
        if e.isdigit() and emol[-1] is '}':
            continue
        emol += [e, '{}'][e.isdigit()]
    return eval(emol.format(*sorted([i for l in A for e in l for i in e])))
