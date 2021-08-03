def create_number_class(alphabet):
    n = len(alphabet)

    class C(int):
        def __new__(cls, s):
            return super().__new__(
                cls, sum(alphabet.index(c) * n**i for i, c in enumerate(s[::-1]))
            )

        def __str__(self):
            s = ""
            while self > 0:
                self, d = divmod(self, n)
                s = alphabet[d] + s
            return s or alphabet[0]

        for op in ['__add__', '__sub__', '__mul__', '__floordiv__']:
            locals()[op] = lambda self, other, op=op: int.__new__(type(self), getattr(int, op)(self, other))

        def convert_to(self, c):
            return int.__new__(c, self)
    return C
