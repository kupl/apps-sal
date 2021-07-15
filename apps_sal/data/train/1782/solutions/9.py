class Simplexer:
    def __init__(self, expression):
        self.expression = expression
        self.pos = 0
    def __iter__(self):
        return self
    def __next__(self):
        length = len(self.expression)
        start = self.pos
        if self.pos == length:
            raise StopIteration
        if self.expression[start] == '"':
            self.pos = start + 1
            while self.pos < length and self.expression[self.pos] != '"': self.pos += 1
            self.pos += 1
            return Token(self.expression[start:self.pos], 'string')
        if self.expression[start] in '+-*/%()=':
            self.pos += 1
            return Token(self.expression[start], 'operator')
        for typ, func in scans:
            if func(self.expression[start]):
                self.pos = start + 1
                while self.pos < length and func(self.expression[self.pos]):
                    self.pos += 1
                value = self.expression[start:self.pos]
                if typ == 'identifier':
                    if value in ('true', 'false'): typ = 'boolean'
                    elif value in keywords: typ = 'keyword'
                return Token(value, typ)

keywords = {'if', 'else', 'for', 'while', 'return', 'func', 'break'}

scans = (
    ('integer', lambda c: c.isdigit()),
    ('whitespace', lambda c: c.isspace()),
    ('identifier', lambda c: c.isalnum() or c in '$_'),
    )

