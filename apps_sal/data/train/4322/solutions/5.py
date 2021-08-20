import re


def body_count(code):
    reg = re.compile('([A-Z][0-9]){5}\\.\\-[A-Z]\\%[0-9]\\.([0-9]){2}\\.')
    return bool(re.search(reg, code))
