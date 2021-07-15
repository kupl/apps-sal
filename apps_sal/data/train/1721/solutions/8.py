def create_number_class(alphabet):
    class Number():
        alph = alphabet
        def __init__(self, numb):
            if type(numb) == str:
                self.value = Number.conv(numb)
            else: self.value = numb
        
        def conv(n):
            base = len(Number.alph)
            r, m = 0, 1
            for i in range(1, len(n)+1):
                r += m * Number.alph.index(n[-i])
                m *= base
            return r
        
        def vnoc(nu):
            r = ''
            base = len(Number.alph)
            if nu == 0:
                return Number.alph[0]
            else:
                while nu > 0:
                    r += Number.alph[nu % base]
                    nu //= base
                return r[::-1]
        
        def convert_to(self, NumClass):
            return NumClass(self.value)
        
        def __add__(self, other):
            return Number(self.value + other.value)
        
        def __sub__(self, other):
            return Number(self.value - other.value)
        
        def __mul__(self, other):
            return Number(self.value * other.value)
        
        def __floordiv__(self, other):
            return Number(self.value // other.value)
        
        def __str__(self):
            return Number.vnoc(self.value)
        
    return Number
