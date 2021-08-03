from itertools import groupby
import re


def fire_and_fury(tweet):
    if set(tweet) > set("EFIRUY") or ("FIRE" not in tweet and "FURY" not in tweet):
        return "Fake tweet."
    return " ".join(translate(group) for group in groupby(re.findall(r"FIRE|FURY", tweet)))


def translate(group):
    word, repeat = group[0], len(tuple(group[1])) - 1
    base, more = {"FURY": ("I am {}furious.", "really "), "FIRE": ("You {}are fired!", "and you ")}[word]
    return base.format(more * repeat)
