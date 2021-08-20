def the_biggest_search_keys(*arg):
    mx = len(max(arg, key=len, default=''))
    return ', '.join(sorted((f"'{e}'" for e in list(arg) + [''] if len(e) == mx)))
