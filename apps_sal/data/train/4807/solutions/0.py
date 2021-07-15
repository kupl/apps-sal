def search_names(logins):
    return list(filter(lambda a: a[0].endswith('_'), logins))
