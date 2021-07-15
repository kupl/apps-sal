def create_number_class(alphabet):
    class C():
        alph = alphabet
        def __init__(self, num):
            self.n = sum(C.alph.find(num[i]) * len(C.alph)**(len(num) - i - 1) for i in range(len(num)))
        def __str__(self):
            return to_str(self.n, C.alph)
        def __add__(self, c):
            inst = C(to_str(self.n + c.n, C.alph))
            return inst
        def __sub__(self, c):
            inst = C(to_str(self.n - c.n, C.alph))
            return inst
        def __mul__(self, c):
            inst = C(to_str(self.n * c.n, C.alph))
            return inst
        def __floordiv__(self, c):
            inst = C(to_str(self.n // c.n, C.alph))
            return inst
        def convert_to(self, Cl):
            inst = Cl(to_str(self.n, Cl.alph))
            return inst
    return C

def to_str(k, alphabet):
    if k == 0:
        return alphabet[0]
    res = ''
    while k > 0:
        res = alphabet[k % len(alphabet)] + res
        k = k // len(alphabet)
    return res
