from re import compile as reCompile
PATTERN = reCompile('(?P<integer>\\d+)|(?P<boolean>true|false)|(?P<string>".*")|(?P<operator>[+*/%()=-])|(?P<keyword>if|else|for|while|return|func|break)|(?P<whitespace>\\s+)|(?P<identifier>[a-zA-Z_$][a-zA-Z0-9_$]*)')


class Simplexer:

    def __init__(self, s):
        self.s = s
        self.pos = 0

    def __iter__(self):
        return self

    def __call__(self):
        return self

    def __next__(self):
        m = PATTERN.match(self.s, self.pos)
        if not m:
            raise StopIteration()
        self.pos = m.end()
        for (name, value) in m.groupdict().items():
            if value:
                return Token(value, name)

    @classmethod
    def simplex(cls, s):
        return cls(s)
