import re


def wheres_wally(string):
    return next((m.start() for m in re.finditer('((?<= )W|^W)ally\\b', string)), -1)
