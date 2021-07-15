import re

def vowel_2_index(string):
    return re.sub(
        re.compile('[euioa]', re.I),
        lambda match: str(match.start() + 1),
        string
    )
