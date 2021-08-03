def my_very_own_split(string, delimiter=None):
    for w in eval('string.split(delimiter)'):
        yield w
