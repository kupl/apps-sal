import re


def increment_string(s):
    return re.sub('\\d+\\Z', lambda m: f'{int(s[m.start():]) + 1}'.zfill(m.end() - m.start()), s) if re.search('\\d\\Z', s) else s + '1'
