def create_number_class(alphabet):
    class CNum:

        doc = {e: i for i, e in enumerate(alphabet)}
        sdc = {v: k for k, v in doc.items()}
        l = len(doc)

        def __init__(self, val):
            self.val = val
            self.int = self.to_int(val)

        def __str__(self):
            return str(self.val)

        def convert_to(self, mod):
            return self.to_str(self.int, mod.sdc, mod.l)

        def to_int(self, val):
            return sum(self.doc[e] * (self.l**i) for i, e in enumerate(val[::-1]))

        def customer(f):
            def wrap(cls, *args):
                return CNum(cls.to_str(f(cls, *args), cls.sdc, cls.l))
            return wrap

        @customer
        def __add__(self, o):
            return self.int + o.int

        @customer
        def __sub__(self, o):
            return self.int - o.int

        @customer
        def __mul__(self, o):
            return self.int * o.int

        @customer
        def __floordiv__(self, o):
            return self.int // o.int

        @staticmethod
        def to_str(val, dic, l, cnum=''):
            while val:
                cnum += dic[val % l]
                val //= l
            return dic[val] if not cnum else cnum[::-1]

    return CNum
