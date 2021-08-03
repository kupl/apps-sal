def the_biggest_search_keys(*keys):
    L = sorted(keys, key=lambda key: (-len(key), key))
    i = next((i for i, key in enumerate(L) if len(key) != len(L[0])), None)
    return str(L[:i])[1:-1] or "''"
