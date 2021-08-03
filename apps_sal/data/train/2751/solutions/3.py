def word_search(query, seq):
    l = [i for i in seq if query.lower() in i.lower()]
    return [l, ['None']][not l]
