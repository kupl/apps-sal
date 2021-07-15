def search(titles, term):
    term = term.casefold()
    return [t for t in titles if term in t.casefold()]
