import re


def get_users_ids(s):
    s = s.lower().replace('#', '')
    return [re.sub('^uid', '', x.strip(), count=1).strip() for x in s.split(',')]
