def create_number_class(alp):
    alphabet = {j: i for i, j in enumerate(alp)}

    class BinClass:
        def __init__(self, text): self.text = text
        def __add__(self, other): return self.op(self.text, other.text, '+')
        def __sub__(self, other): return self.op(self.text, other.text, '-')
        def __mul__(self, other): return self.op(self.text, other.text, '*')
        def __floordiv__(self, other): return self.op(self.text, other.text, '//')
        def __str__(self): return self.text

        def op(self, a, b, sign): return BinClass(self.from_decimal(eval('{} {} {}'.format(self.to_decimal(a), sign, self.to_decimal(b)))) or alp[0])
        def convert_to(self, base): return base(self.text).from_decimal(self.to_decimal(self.text))
        def to_decimal(self, s): return sum(alphabet[j] * (len(alp) ** (len(s) - 1 - i)) for i, j in enumerate(s))
        from_decimal = lambda self, s, li=[]: self.from_decimal(s // len(alp), li + [s % len(alp)]) if s else ''.join([alp[int(i)] for i in li[::-1]])
    return BinClass
