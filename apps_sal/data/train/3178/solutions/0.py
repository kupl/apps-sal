import re

PATTERN = re.compile(r'(?P<first>(?:(?<=[.!?] )|^)\w+)|(?P<other>\w+)')


def pete_talk(speech, ok=[]):

    def watchYourMouth(m):
        w = (m.group("first") or m.group("other")).lower()
        if w not in ok and len(w) > 1:
            w = w[0] + '*' * (len(w) - 2) + w[-1]
        if m.group("first"):
            w = w.capitalize()
        return w

    ok = set(map(str.lower, ok))
    return PATTERN.sub(watchYourMouth, speech)
