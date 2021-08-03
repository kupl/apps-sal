import re


class Simplexer:
    regex = re.compile("|".join("(?P<{}>{})".format(token_type, regex) for token_type, regex in (
        ("integer", r'\d+'),
        ("boolean", r'\b(?:true|false)\b'),
        ("string", r'"[^"]*"'),
        ("operator", r'[*/%()=+-]'),
        ("keyword", r'\b(?:if|else|for|while|return|func|break)\b'),
        ("whitespace", r'\s+'),
        ("identifier", r'[a-zA-Z_$][a-zA-Z0-9_$]*'),
    )))

    def __init__(self, expression):
        self.iter = self.regex.finditer(expression)

    def __iter__(self):
        return self

    def __next__(self):
        match = next(self.iter)
        return Token(match.group(0), match.lastgroup)
