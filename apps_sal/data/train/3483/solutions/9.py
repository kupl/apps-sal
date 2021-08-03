import re


def string_parse(string):
    if not isinstance(string, str):
        return 'Please enter a valid string'

    def repl(Match):

        s = Match[0]
        n = len(s)
        c = s[0]

        return s if n <= 2 else c * 2 + f'[{c * (n - 2)}]'
    return re.sub(r'(\w)\1*', repl, string)
