from re import compile as reCompile

PATTERN = reCompile(r'(?i)[-_]([a-z])')

def to_camel_case(text):
    return PATTERN.sub(lambda m: m.group(1).upper(), text)

