def sort_array(xs):
    es = sorted((x for x in xs if x % 2 == 0))
    os = sorted((x for x in xs if x % 2 != 0), reverse=True)
    return [(es if x % 2 == 0 else os).pop() for x in xs]
