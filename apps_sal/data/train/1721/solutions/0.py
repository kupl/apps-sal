def create_number_class(alphabet):
    n = len(alphabet)

    class Number(object):

        def __init__(self, s):
            if isinstance(s, str):
                v = 0
                for c in s:
                    v = v * n + alphabet.index(c)
            else:
                v = s
            self.value = v

        def __add__(self, other):
            return Number(self.value + other.value)

        def __sub__(self, other):
            return Number(self.value - other.value)

        def __mul__(self, other):
            return Number(self.value * other.value)

        def __floordiv__(self, other):
            return Number(self.value // other.value)

        def __str__(self):
            ret = []
            v = int(self.value)
            while v:
                (v, r) = divmod(v, n)
                ret.append(alphabet[r])
            return ''.join(reversed(ret or alphabet[0]))

        def convert_to(self, cls):
            return cls(self.value)
    return Number
