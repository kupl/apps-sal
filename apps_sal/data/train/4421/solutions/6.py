import re
def to_seconds(t): return sum(int(j) * i for i, j in zip([3600, 60, 1], t.split(':')))if re.sub(r'^\d{2}:[0-5][0-9]:[0-5][0-9]$', '', t) == ''else None
