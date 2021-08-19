def only_duplicates(string):
    return ''.join((s for s in string if string.count(s) > 1))
