import re


def wheres_wally(string):
    match = re.search(r"(?<!\S)\bWally\b", string)
    return match.start() if match else -1
