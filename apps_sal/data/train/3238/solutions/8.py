def get_users_ids(string):
    return [word.strip()[3:].strip() for word in string.replace('#', '').lower().split(', ')]
