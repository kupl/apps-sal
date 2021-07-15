import re

def short_form(s):
    regex = re.compile("(?!^)[aeiou](?!$)", re.I)
    return re.sub(regex, "", s)

