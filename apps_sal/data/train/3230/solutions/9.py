def the_biggest_search_keys(*keywords):
    return ', '.join(sorted((f"'{x}'" for x in keywords if len(x) == max(map(len, keywords))))) if keywords else "''"
