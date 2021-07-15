def word_search(query, seq):
    query = query.lower()
    result = [x for x in seq if query in x.lower()]
    return result if result else ['None']
