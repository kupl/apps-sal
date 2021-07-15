funcs = [
'__int__', '__index__', '__floor__', '__ceil__', '__trunc__', '__round__',

'__abs__',
'__pos__', '__neg__', '__invert__',

'__add__', '__sub__', '__mul__', '__floordiv__', '__truediv__', '__mod__', '__pow__',
'__and__', '__or__', '__xor__', '__lshift__', '__rshift__',

'__radd__', '__rsub__', '__rmul__', '__rfloordiv__', '__rtruediv__', '__rmod__', '__rpow__',
'__rand__', '__ror__', '__rxor__', '__rlshift__', '__rrshift__',

'__eq__', '__ne__', '__ge__', '__le__', '__gt__', '__lt__',

'numerator', 'denominator', 'real', 'imag', 'conjugate', 'bit_length', 'from_bytes']

CastedInt = type('', (int,), {func: lambda self, *args, func=func, **kwargs:
    self.__class__(getattr(super(CastedInt, self), func)(*args, **kwargs)) for func in funcs})

BaseNumber = type('', (CastedInt,), {
    '__new__': lambda cls, n: super(BaseNumber, cls).__new__(
                                    cls, n if isinstance(n, int) else
                                       sum(cls.alphabet.index(c) * cls.base ** i for i, c in enumerate(n[::-1]))),
    '__str__': lambda self: self and str(self//self.base).lstrip(self.alphabet[0]) + self.alphabet[self%self.base] or self.alphabet[0],
    'convert_to': lambda self, other: other(self)
})

create_number_class = lambda alphabet: type('', (BaseNumber,), {'base': len(alphabet), 'alphabet': alphabet})
