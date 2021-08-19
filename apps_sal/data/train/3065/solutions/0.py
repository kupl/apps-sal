import re
SKIPERS = re.compile('|'.join(['\\\\*.*?\\*/', '--.*?(\n|$)', "''"]))


def get_textliterals(code):
    code = SKIPERS.sub(lambda m: 'x' * len(m.group()), code.rstrip())
    if code.count("'") % 2:
        code += "'"
    return [(m.start(), m.end()) for m in re.finditer("'.+?'", code, flags=re.DOTALL)]
