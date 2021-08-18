def get_users_ids(s):
    s = s.replace('
    r=[e.rstrip().strip() for e in s.split(', ')]
    r=[e[3:].strip() if e[:3] == 'uid' else e for e in r]
    return r
