import re


def get_textliterals(pv_code):
    return [(match.start(1), match.end(1)) for match in re.finditer(r"(?:--[^\n]*\n?|/\*.*?\*/|((?:'[^']*')+|'[^']*$)|.)", pv_code, re.DOTALL) if match.group(1)]
