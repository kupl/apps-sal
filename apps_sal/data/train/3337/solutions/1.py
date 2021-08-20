from re import findall


def bracket_buster(s):
    return 'Take a seat on the bench.' if type(s) is not str else findall('\\[(.*?)\\]', s)
