def search_names(logins):
    return(list(filter(lambda s: s[0][-1] == "_", logins)))
