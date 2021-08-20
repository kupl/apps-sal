def get_strings(s):
    return ','.join((k + ':' + s.lower().count(k) * '*' for k in dict.fromkeys(s.lower().replace(' ', ''))))
