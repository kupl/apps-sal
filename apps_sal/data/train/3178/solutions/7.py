import re

def pete_talk(speech, ok=()):
    oks = [w.lower() for w in ok]
    upper_first = re.sub('^[a-z]', lambda c: c.group().upper(), speech, 1)
    lower2uppercased = re.sub('[A-Z]{2,}|[.!?] [a-z]', lambda w: w.group().title(), upper_first)
    lower_punc = re.sub(r'[^.!?] [A-Z]', lambda w: w.group().lower(), lower2uppercased)

    def xx(g):
        w = g.group()
        return f'{w[0]}{(len(w)-2) * "*"}{w[-1]}' if w.lower() not in oks else w

    long_words = re.sub('[a-zA-Z]{2,}', xx, lower_punc)

    return long_words
