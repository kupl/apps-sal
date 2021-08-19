from re import findall


class Simplexer(object):

    def __init__(self, expression):
        self.current = 0
        self.result = []
        for x in findall('(".*"|true|false|\\d+|[a-zA-Z]+|[+\\-()\\/*=]|\\s+)', expression):
            if x[0] == '"':
                type = 'string'
            elif x.isdigit():
                type = 'integer'
            elif x.isspace():
                type = 'whitespace'
            elif x in '+-()/*=':
                type = 'operator'
            elif x in ('true', 'false'):
                type = 'boolean'
            elif x in ('if', 'break', 'return', 'for', 'else'):
                type = 'keyword'
            else:
                type = 'identifier'
            self.result.append(Token(x, type))

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == len(self.result):
            raise StopIteration
        res = self.result[self.current]
        self.current += 1
        return res
