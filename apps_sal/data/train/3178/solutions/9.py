from re import sub


def capital(x):
    return x.group().capitalize()


def censor(x):
    return x[0] + '*' * (len(x) - 2) + x[-1]


def pete_talk(speech, ok=[]):
    okay = set(map(str.lower, ok)).__contains__

    def check(x):
        return x.group() if okay(x.group().lower()) else censor(x.group())
    return sub('[\\w\\s*:,;]+(?:[\\.?!](?:\\s|$)|$)', capital, sub('\\w{3,}', check, speech))
