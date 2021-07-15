def word_search(query, seq):
    result =  [word for word in seq if query.lower() in word.lower()]
    return result if result else ['None']
