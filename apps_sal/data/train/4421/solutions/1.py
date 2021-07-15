import re


def to_seconds(time):
    if bool(re.match('[0-9][0-9]:[0-5][0-9]:[0-5][0-9]\Z', time)):
        return int(time[:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:8])
    else:
        return None
