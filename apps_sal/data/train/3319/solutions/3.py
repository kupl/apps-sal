from re import compile as reCompile
PATTERN = reCompile('(?i)[-_]([a-z])')


def to_camel_case(text):
    return PATTERN.sub(lambda m: m.group(1).upper(), text)
