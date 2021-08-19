import re


def validate(msg):
    return bool(re.match('^MDZHB \\d\\d \\d\\d\\d [A-Z]+ \\d\\d \\d\\d \\d\\d \\d\\d$', msg))
