import re


def time_correct(time_string):
    if time_string in ('', None):
        return time_string
    if not re.fullmatch('\\d\\d:\\d\\d:\\d\\d', time_string):
        return None
    (h, m, s) = map(int, time_string.split(':'))
    total_seconds = 3600 * h + 60 * m + s
    final_seconds = total_seconds % 60
    final_minutes = total_seconds // 60 % 60
    final_hours = total_seconds // 3600 % 24
    return f'{final_hours:02d}:{final_minutes:02d}:{final_seconds:02d}'
