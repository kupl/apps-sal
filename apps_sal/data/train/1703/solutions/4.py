class BFCore(object):
    STR_C = ''

    def __init__(self, delta=0, val=''):
        self.delta = delta
        self.val = val

    def __repr__(self):
        return '{}({},{})'.format(self.__class__.__name__, self.val, self.delta)

    def __bool__(self):
        return True

    def toC(self):
        return ' ' * self.delta + self.STR_C


class ValMov(BFCore):

    def toC(self):
        return self.STR_C.format(' ' * self.delta, '+' if self.val > 0 else '-', abs(self.val))

    def __iadd__(self, n):
        self.val += n
        return self

    def __bool__(self):
        return self.val != 0


class Val(ValMov):
    STR_C = '{}*p {}= {};\n'


class Mov(ValMov):
    STR_C = '{}p {}= {};\n'


class LoopOpen(BFCore):
    STR_C = 'if (*p) do {\n'


class LoopClose(BFCore):
    STR_C = '} while (*p);\n'


class Input(BFCore):
    STR_C = '*p = getchar();\n'


class Output(BFCore):
    STR_C = 'putchar(*p);\n'


def brainfuck_to_c(source):
    (lst, delta) = ([BFCore()], 0)
    for c in source:
        if c in '-+':
            if isinstance(lst[-1], Val):
                lst[-1] += 1 if c == '+' else -1
                if not lst[-1]:
                    del lst[-1]
            else:
                lst.append(Val(delta, 1 if c == '+' else -1))
        elif c in '<>':
            if isinstance(lst[-1], Mov):
                lst[-1] += 1 if c == '>' else -1
                if not lst[-1]:
                    del lst[-1]
            else:
                lst.append(Mov(delta, 1 if c == '>' else -1))
        elif c == '[':
            lst.append(LoopOpen(delta))
            delta += 2
        elif c == ']':
            delta -= 2
            if delta < 0:
                return 'Error!'
            if isinstance(lst[-1], LoopOpen):
                del lst[-1]
            else:
                lst.append(LoopClose(delta))
        elif c == ',':
            lst.append(Input(delta))
        elif c == '.':
            lst.append(Output(delta))
    return 'Error!' if delta != 0 else ''.join((tok.toC() for tok in lst))
