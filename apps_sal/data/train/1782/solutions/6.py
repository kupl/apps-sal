from itertools import chain


class Simplexer(object):
    BOOLS = ['true', 'false']
    KEYWORDS = ['if', 'else', 'for', 'while', 'return', 'func', 'break']
    OPERATORS = '+-*/%()='
    SPACE = ' \n\t\\c'
    NUMBER = '0123456789'
    CHAR = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_$'

    def __init__(self, expression):
        self.expression = expression
        self.__data = iter(expression)

    def __iter__(self):
        self.__data = iter(self.expression)
        return self

    def __next__(self):
        token = self._nextc()
        if token in self.OPERATORS:
            return Token(token, 'operator')
        if token in self.SPACE:
            while self._peekc() in self.SPACE:
                token += self._nextc()
            return Token(token, 'whitespace')
        if token == '"':
            token += self._nextc()
            while token[-1] != '"':
                token += self._nextc()
            return Token(token, 'string')
        if token in self.NUMBER:
            while self._peekc() in self.NUMBER:
                token += self._nextc()
            return Token(token, 'integer')
        if token in self.CHAR:
            while self._peekc() in self.CHAR + self.NUMBER:
                token += self._nextc()
            if token in self.BOOLS:
                return Token(token, 'boolean')
            if token in self.KEYWORDS:
                return Token(token, 'keyword')
            return Token(token, 'identifier')

    def _nextc(self):
        return next(self.__data)

    def _peekc(self):
        try:
            char = next(self.__data)
            self.__data = chain([char], self.__data)
        except:
            char = 'END'
        return char
