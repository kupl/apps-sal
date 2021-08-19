def search_names(logins):
    return filter(lambda x: x[0][-1] == '_', logins)
