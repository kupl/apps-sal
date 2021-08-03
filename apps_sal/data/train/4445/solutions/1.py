import re


def is_haiku(text):
    def count_syllables(line):
        return len(re.findall(r'[aeiouy]{2,}|[aiouy]|e\B|\b[^\Waeiouy]*e\b', line, re.I))
    return tuple(map(count_syllables, text.splitlines())) == (5, 7, 5)
