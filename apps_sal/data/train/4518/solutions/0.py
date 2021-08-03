from re import compile


def wheres_wally(string):
    m = compile('(^|.*[\s])(Wally)([\.,\s\']|$)').match(string)
    return m.start(2) if m else -1
