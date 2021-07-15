import re 

def password(string):
    patterns = (r'[A-Z]', r'[a-z]', r'[0-9]', r'.{8,}')
    return all([re.search(pattern, string) for pattern in patterns])
