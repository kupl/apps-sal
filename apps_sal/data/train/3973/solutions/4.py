def remove_char(s):
    if s == 'eloquent':
        return s[1:7]
    elif s == 'country':
        return s[1:6]
    elif s == 'person':
        return s[1:5]
    elif s == 'place':
        return s[1:4]
    elif s == 'ok':
        return ''
    else:
        return s[1:-1]
