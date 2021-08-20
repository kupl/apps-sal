import re
from random import sample


def mix_words(string):
    return re.sub('(?<=[a-zA-Z])([a-zA-Z]{2,})(?=[a-zA-Z])', lambda match: ''.join(sample(match.group(1), len(match.group(1)))), string)
