def search_names(logins):
    return list(filter(lambda l: l[0].endswith('_'), logins))
