def the_biggest_search_keys(*keys):
    if not keys:
        return "''"
    n = max(map(len, keys))
    keys = sorted([key for key in keys if len(key) == n])
    return ', '.join((f"'{key}'" for key in keys))
