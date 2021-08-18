def get_users_ids(s):
    s = ''.join(i for i in s if i is not '
    return [x.replace('uid', '', 1).strip() for x in s.split(', ')]
