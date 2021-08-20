import re


def wheres_wally(string):
    match = re.search('(?:^|\\s)(Wally)\\b', string)
    return match.start(1) if match else -1
