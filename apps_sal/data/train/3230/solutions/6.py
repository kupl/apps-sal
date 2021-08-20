def the_biggest_search_keys(*keys):
    (biggest, max_len) = ([], 0)
    for key in keys:
        key_len = len(key)
        if key_len == max_len:
            biggest.append(key)
        elif key_len > max_len:
            (biggest, max_len) = ([key], key_len)
    return ', '.join(("'{}'".format(key) for key in sorted(biggest))) or "''"
