def search_names(logins):
    return filter(lambda eml: eml[0][-1] == "_", logins)
