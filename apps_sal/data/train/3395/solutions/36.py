def remove_duplicate_words(s):
    arr = s.split()
    res_list = []
    for elem in arr:
        if not elem in res_list:
            res_list.append(elem)
    return ' '.join(res_list)
