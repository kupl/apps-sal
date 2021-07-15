get_users_ids=lambda s:[w.strip()[3:].strip()for w in s.replace('#','').lower().split(',')]
