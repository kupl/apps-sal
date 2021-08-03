import re
from random import shuffle


def mix_words(string):
    def mix(s):
        s = list(s)
        shuffle(s)
        return "".join(s)

    return re.sub("(\w)(\w{2,})(\w)", lambda m: m.group(1) + mix(m.group(2)) + m.group(3), string)
