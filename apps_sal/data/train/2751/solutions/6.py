def word_search(query, seq):
    query = query.lower()
    return [a for a in seq if query in a.lower()] or ['None']
