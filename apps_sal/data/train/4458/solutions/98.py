import re

def time_correct(t):
    if not t: return t

    pattern = r'\d{2}:\d{2}:\d{2}'
    
    if not re.match(pattern, t): return None

    hours, minutes, seconds = map(int, t.split(':'))

    minutes, seconds = minutes + (seconds // 60), seconds % 60
    hours, minutes = (hours + (minutes // 60)) % 24, minutes % 60

    return '{:0>2}:{:0>2}:{:0>2}'.format(hours, minutes, seconds)
