def the_biggest_search_keys(*keys):
    if not keys:
        keys = ['']
    longest_key_length = max(map(len, keys))
    return ', '.join(sorted(("'%s'" % key for key in keys if len(key) == longest_key_length)))
