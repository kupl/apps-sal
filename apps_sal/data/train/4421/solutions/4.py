import re


def to_seconds(time):
    match = re.fullmatch('(\\d{2}):([0-5][0-9]):([0-5][0-9])', time)
    return int(match.group(1)) * 3600 + int(match.group(2)) * 60 + int(match.group(3)) if match else None
