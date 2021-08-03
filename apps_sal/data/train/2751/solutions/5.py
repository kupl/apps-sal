def word_search(q, l):
    return [w for w in l if q.lower() in w.lower()] or ['None']
