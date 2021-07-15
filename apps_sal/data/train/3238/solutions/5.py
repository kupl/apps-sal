def get_users_ids(s):
    return [x.strip()[3:].strip() for x in s.replace('#','').lower().split(',')]
