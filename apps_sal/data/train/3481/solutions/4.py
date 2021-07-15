def get_char_count(s):
    lst = filter(lambda x: x.isalnum(), s.lower())
    result = {}
    for i in set(lst):
        result[s.lower().count(i)] = sorted(result.get(s.lower().count(i), []) + [i])
    return result
