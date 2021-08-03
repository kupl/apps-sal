import re

insults_regexp = re.compile("(bad|mean|ugly|horrible|hideous)", re.IGNORECASE)


def filter_words(phrase):
    return insults_regexp.sub("awesome", phrase)
