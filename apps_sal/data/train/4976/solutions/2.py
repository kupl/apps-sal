search = lambda titles, term: list(filter(lambda title: term.lower() in title.lower(), titles))
