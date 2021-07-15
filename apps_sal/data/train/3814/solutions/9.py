def get_military_time(_s):
    if 'A' in _s and _s.startswith('12'):
        return '00' + _s[2:-2]
    if 'P' in _s and not _s.startswith('12'):
        return str(int(_s[:2])+12) + _s[2:-2]
    return _s[:-2]
