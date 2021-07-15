def search(titles, term):
    return list(t for t in titles if term.lower() in t.lower())
