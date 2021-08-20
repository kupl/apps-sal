def body_count(s):
    return bool(__import__('re').search('(?:[A-Z]\\d){5}\\.-[A-Z]%\\d\\.\\d\\d\\.', s))
