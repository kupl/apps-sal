def word_search(query, seq):
    query = query.lower()
    return [word for word in seq if query in word.lower()] or ["None"]
