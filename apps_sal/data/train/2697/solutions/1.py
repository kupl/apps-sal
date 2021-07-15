import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)
