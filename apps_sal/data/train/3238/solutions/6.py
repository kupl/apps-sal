get_users_ids = lambda string: [x.strip()[3:].strip() for x in string.lower().replace('#','').split(', ')]
