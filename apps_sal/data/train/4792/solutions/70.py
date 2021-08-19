"""A primitive parser based on Haskell's Text.ParserCombinators.ReadP
This is super complicated don't do this"""
from operator import methodcaller


def parse_float(string):
    if isinstance(string, list):
        string = ''.join(string)
    p = NumParser(string)
    res = p.parse_float()
    p.eof()
    if p.failed:
        return None
    return res


class Parser(object):
    """Base parser class
    Meant to be inherited by other classes

    TODO:
        - Implement `try`
        - Implement some sort of Applicative (especially Alternative <|>)
        - if self.failed == True, should halt any parsing
        -   You shouldn't need to constantly check for failure
    """

    def __init__(self, string):
        self.string = string
        self.failed = False

    def __repr__(self):
        return f'{self.__class__.__name__}({self.string}, {self.failed})'

    def look(self):
        """Returns a copy of self (with new_parser.failed == True)
        For running a parser without affecting self
        """
        return type(self)(self.string)

    def get(self):
        """Gets the first character of the string"""
        if len(self.string) == 0 or self.failed:
            self.failed = True
            return None
        char = self.string[0]
        self.string = self.string[1:]
        return char

    def eof(self):
        """Succeeds iff there is no more string to consume"""
        if self.failed:
            return None
        self.failed = len(self.string) > 0

    def satisfy(self, func):
        """Consumes and returns the next character, if it satisfies the specified predicate
        func :: char -> bool
        """
        char = self.get()
        if self.failed:
            return None
        res = func(char)
        if isinstance(res, bool) and res:
            return char
        self.string = char + self.string
        self.failed = True
        return None

    def option(self, default, methodname, *args, **kwargs):
        """Will either parse self.methodname(*args, **kwargs) or return default on failure
        If failure, does not consume any characters, and self.failed remains as it was before
        e.g.,
        self = Parser("hi")
        1. self.option("c", "satisfy", str.islower) -> "h"
        2. self.option("c", "satisfy", str.isupper) -> "c"
        """
        looker = self.look()
        func = methodcaller(methodname, *args, **kwargs)
        func(looker)
        if looker.failed:
            return default
        return func(self)

    def char(self, character, insensitive=False):
        """self.char(character) == self.satisfy(ch.__eq__)
        self.char(character, insensitive=True) == self.satisfy(lambda x: x.casefold() == character.casefold())
        """
        if insensitive:
            return self.satisfy(lambda x: x.casefold() == character.casefold())
        return self.satisfy(character.__eq__)

    def many(self, methodname, *args, **kwargs):
        """Will parse while predicate holds true
        Returns list of results of predicate
        Never fails (can return [])
        """
        func = methodcaller(methodname, *args, **kwargs)
        results = []
        while not self.failed:
            res = func(self)
            if self.failed:
                self.failed = False
                break
            results.append(res)
        return results

    def many1(self, methodname, *args, **kwargs):
        """Same as many but requires at least one success"""
        func = methodcaller(methodname, *args, **kwargs)
        res = func(self)
        if self.failed:
            return None
        results = [res]
        results.extend(self.many(methodname, *args, **kwargs))
        return results


class NumParser(Parser):
    """A basic example of a Parser subclass
    Parses numbers (ints and floats)
    """

    def parse_int(self, signed=True):
        """Parses an integer
        If signed is True, allows a leading (-), otherwise it doesn't
        """
        sign = -1 if signed and self.option('+', 'char', '-') == '-' else 1
        digits = self.many1('satisfy', str.isdigit)
        if self.failed:
            return None
        return sign * int(''.join(digits))

    def parse_float(self):
        """Parses floats"""
        intpart = self.parse_int()
        if self.failed:
            return None
        sign = -1 if intpart < 0 else 1
        self.option(None, 'char', '.')
        floatpart = self.option(['0'], 'many1', 'satisfy', str.isdigit)
        floatpart = int(''.join(floatpart)) / 10 ** len(floatpart)
        if self.option(None, 'char', 'e', insensitive=True) is not None:
            exppart = self.parse_int()
        else:
            exppart = 0
        if self.failed:
            return None
        return (intpart + sign * floatpart) * 10 ** exppart
