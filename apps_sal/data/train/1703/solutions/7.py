import re


class Token(object):
    ARITH = 1
    POINTER = 2
    GETCHAR = 3
    PUTCHAR = 4
    OPEN = 5
    CLOSE = 6

    def __init__(self, mode=None, indent=None, value=None):
        self.mode = mode
        self.value = value
        self.indent = indent

    def __str__(self):
        if self.mode == self.ARITH:
            sign = '+' if self.value > 0 else '-'
            return '{}*p {}= {};\n'.format(self.indent, sign, abs(self.value))
        if self.mode == self.POINTER:
            sign = '+' if self.value > 0 else '-'
            return '{}p {}= {};\n'.format(self.indent, sign, abs(self.value))
        if self.mode == self.GETCHAR:
            return self.indent + '*p = getchar();\n'
        if self.mode == self.PUTCHAR:
            return self.indent + 'putchar(*p);\n'
        if self.mode == self.OPEN:
            return self.indent + 'if (*p) do {\n'
        if self.mode == self.CLOSE:
            return self.indent + '} while (*p);\n'
        return ''


class BF(object):
    ARITH = 1
    POINTER = 2
    GETCHAR = 3
    PUTCHAR = 4
    OPEN = 5
    CLOSE = 6

    def __init__(self, source_code):
        self.indent = ''
        self.source_code = source_code
        self.tokens = [Token()]
        self.error = False

    def convert_to_c(self):
        try:
            for c in self.source_code:
                self.convert_one_char(c)
        except ValueError:
            return 'Error!'
        if self.indent:
            return 'Error!'
        return ''.join(map(str, self.tokens))

    def convert_one_char(self, c):
        if c in '+-':
            if self.tokens[-1].mode != self.ARITH:
                self.tokens.append(Token(self.ARITH, self.indent, 0))
            if c == '+':
                self.tokens[-1].value += 1
            else:
                self.tokens[-1].value -= 1
            if not self.tokens[-1].value:
                del self.tokens[-1]
        elif c in '><':
            if self.tokens[-1].mode != self.POINTER:
                self.tokens.append(Token(self.POINTER, self.indent, 0))
            if c == '>':
                self.tokens[-1].value += 1
            else:
                self.tokens[-1].value -= 1
            if not self.tokens[-1].value:
                del self.tokens[-1]
        elif c == ',':
            self.tokens.append(Token(self.GETCHAR, self.indent, 0))
        elif c == '.':
            self.tokens.append(Token(self.PUTCHAR, self.indent, 0))
        elif c == '[':
            self.tokens.append(Token(self.OPEN, self.indent, 0))
            self.indent += '  '
        elif c == ']':
            if not self.indent:
                raise ValueError
            self.indent = self.indent[:-2]
            if self.tokens[-1].mode == self.OPEN:
                del self.tokens[-1]
            else:
                self.tokens.append(Token(self.CLOSE, self.indent, 0))


def brainfuck_to_c(source_code):
    bf = BF(source_code)
    return bf.convert_to_c()
