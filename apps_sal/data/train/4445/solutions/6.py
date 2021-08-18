import re

syllables = re.compile(r'[aeyuio]+[^aeyuio ]*((?=e\b)e)?', flags=re.I)


def is_haiku(text):
    return [5, 7, 5] == [check(s) for s in text.split("\n")]


def check(s):
    return sum(1 for _ in syllables.finditer(s))
