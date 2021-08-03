import re


class Simplexer(object):

    ORDERED_TOKENS = [{"type": "integer", "reg": r'\d+'},
                      {"type": "boolean", "reg": r'true|false'},
                      {"type": "string", "reg": r'\".*\"'},
                      {"type": "operator", "reg": r'[-+*/%\)\(=]'},
                      {"type": "keyword", "reg": r'if|else|for|while|return|func|break'},
                      {"type": "whitespace", "reg": r'\s+'},
                      {"type": "identifier", "reg": r'[$_a-zA-Z][$\w]*'}]

    PATTERN = re.compile(r'|'.join("(?P<{}>{})".format(dct["type"], dct["reg"]) for dct in ORDERED_TOKENS))

    def __init__(self, s): self.iterable = Simplexer.PATTERN.finditer(s)

    def __iter__(self): return self

    def __next__(self):
        for m in self.iterable:
            for k, s in m.groupdict().items():
                if s is None:
                    continue
                return Token(s, k)
        raise StopIteration
