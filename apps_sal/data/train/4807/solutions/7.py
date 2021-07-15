def search_names(logins):
    return filter(lambda l: l[0].endswith('_'), logins)
