import re


def wheres_wally(string):
    match = re.compile("(^|.*[\\s])(Wally)([\\.,\\s\\']|$)").match(string)
    return match.start(2) if match else -1
