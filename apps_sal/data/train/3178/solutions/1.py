import re


def pete_talk(speech, ok=()):
    ok = {word.lower() for word in ok}

    def sub(m):
        s = m.group()
        if s in ok:
            return s
        return s[0] + '*' * (len(s) - 2) + s[-1]
    return re.sub('[a-z][^.?!]+', lambda m: re.sub('\\w{3,}', sub, m.group()).capitalize(), speech.lower())
