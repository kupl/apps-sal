class Simplexer(object):

    def __init__(self, expression):
        self.tokens = []
        l = list(expression)[::-1]
        while l:
            t = l.pop()
            if t in '+-*/%()=':
                ttype = 'operator'
            elif t.isspace():
                ttype = 'whitespace'
                while l and l[-1].isspace():
                    t += l.pop()
            elif t.isdigit():
                ttype = 'integer'
                while l and l[-1].isdigit():
                    t += l.pop()
            elif t == '"':
                ttype = 'string'
                while l and l[-1] != '"':
                    t += l.pop()
                t += l.pop()
            else:
                while l and (not l[-1].isspace()) and (not l[-1] in '+-*/%()='):
                    t += l.pop()
                ttype = 'boolean' if t in 'true false' else 'keyword' if t in 'if else for while return func and break'.split() else 'identifier'
            self.tokens.append(Token(t, ttype))
        self.tokens = self.tokens[::-1]

    def __iter__(self):
        return iter(self.tokens[::-1])

    def __next__(self):
        if self.tokens:
            return self.tokens.pop()
        raise StopIteration()
