brackets = __import__('re').compile('\\[(.*?)\\]').findall


def bracket_buster(string):
    return brackets(string) if type(string) == str else 'Take a seat on the bench.'
