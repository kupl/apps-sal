import re


class Simplexer(object):
    ORDERED_TOKENS = [{'type': 'integer', 'reg': '\\d+'}, {'type': 'boolean', 'reg': 'true|false'}, {'type': 'string', 'reg': '\\".*\\"'}, {'type': 'operator', 'reg': '[-+*/%\\)\\(=]'}, {'type': 'keyword', 'reg': 'if|else|for|while|return|func|break'}, {'type': 'whitespace', 'reg': '\\s+'}, {'type': 'identifier', 'reg': '[$_a-zA-Z][$\\w]*'}]
    PATTERN = re.compile('|'.join(('(?P<{}>{})'.format(dct['type'], dct['reg']) for dct in ORDERED_TOKENS)))

    def __init__(self, s):
        self.iterable = Simplexer.PATTERN.finditer(s)

    def __iter__(self):
        return self

    def __next__(self):
        for m in self.iterable:
            for (k, s) in m.groupdict().items():
                if s is None:
                    continue
                return Token(s, k)
        raise StopIteration
