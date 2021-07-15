def search(titles, term): 
    term = term.lower()
    return [s for s in titles if term in s.lower()]
