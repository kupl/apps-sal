import re
def increment_string(s): return re.sub(r'\d+\Z', lambda m: f'{int(s[m.start():]) + 1}'.zfill(m.end() - m.start()), s) if re.search(r'\d\Z', s) else s + '1'
