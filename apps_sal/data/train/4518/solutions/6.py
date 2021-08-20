import re


def wheres_wally(string):
    match = re.search('(?<!\\S)\\bWally\\b', string)
    return match.start() if match else -1
