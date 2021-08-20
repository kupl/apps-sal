import math


def make_readable(seconds):
    hours = math.floor(seconds / (60 * 60))
    seconds -= hours * 60 * 60
    minutes = math.floor(seconds / 60)
    seconds -= minutes * 60
    out = ''
    if hours < 10:
        out += '0'
    out += str(int(hours)) + ':'
    if minutes < 10:
        out += '0'
    out += str(int(minutes)) + ':'
    if seconds < 10:
        out += '0'
    out += str(int(seconds))
    return out
