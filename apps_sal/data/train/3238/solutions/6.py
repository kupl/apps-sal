def get_users_ids(string): return [x.strip()[3:].strip() for x in string.lower().replace('#', '').split(', ')]
