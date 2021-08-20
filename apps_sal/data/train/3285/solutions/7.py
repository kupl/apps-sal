import re


def trump_detector(trump_speech):
    return (lambda lst: round(sum(lst) / len(lst), 2))([len(t[1]) for t in re.findall('([aeiou])(\\1*)', trump_speech, re.I)])
