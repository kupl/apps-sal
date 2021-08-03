def get_users_ids(s): return [w.strip()[3:].strip()for w in s.replace('#', '').lower().split(',')]
