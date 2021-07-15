def word_search(query, seq):
    return [i for i in seq if query.lower() in i.lower()] or ['None']
