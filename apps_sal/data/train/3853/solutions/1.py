from itertools import cycle
import re

def numeric_formatter(template, source="1234567890"):
    gen = cycle(source)
    return re.sub(r'[a-zA-Z]', lambda m: next(gen), template)
