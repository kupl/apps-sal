def double_check(s):
    return bool(__import__('re').search('(?i)(.)\\1', s))
