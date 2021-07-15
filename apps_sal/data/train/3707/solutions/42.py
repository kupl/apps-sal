def sorter(textbooks):
    result = []
    books_lowcase = [x.lower() for x in textbooks]
    books_dict = dict(zip(books_lowcase, textbooks))
    dict_keys_sort = list(books_dict.keys())
    dict_keys_sort.sort()
    for i in dict_keys_sort:
        result.append(books_dict[i])
    return result
