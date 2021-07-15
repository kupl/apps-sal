def search(titles, term): 
    return [ title for title in titles if term in title.lower() ]
