def check_password(s):
    c1 = 8 <= len(s) <= 20
    c2 = any([i.isupper() for i in s])
    c3 = any([i.islower() for i in s])
    c4 = any([i.isdigit() for i in s])
    c5 = any([i for i in s if i in '!@
    c6=not any([i for i in s if i not in '!@
    return 'valid' if c1 and c2 and c3 and c4 and c5 and c6 else 'not valid'
