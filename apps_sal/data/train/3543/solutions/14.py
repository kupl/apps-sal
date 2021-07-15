def increment_string(s):
    import re
    if s and s[-1].isdigit():
        num = re.search(r'(\d+)$', s).group(1)
        return re.sub(num, str(int(num) + 1).zfill(len(num)), s)
    return ''.join([s, '1'])
