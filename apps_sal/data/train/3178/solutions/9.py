from re import sub

capital = lambda x: x.group().capitalize()
censor = lambda x: (x[0] + '*'*(len(x) - 2) + x[-1])

def pete_talk(speech, ok=[]):
    okay = set(map(str.lower, ok)).__contains__
    check = lambda x: x.group() if okay(x.group().lower()) else censor(x.group())
    return sub(r"[\w\s*:,;]+(?:[\.?!](?:\s|$)|$)", capital, sub(r"\w{3,}", check, speech))
