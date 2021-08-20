def create_number_class(alphabets):
    bases = len(alphabets)

    class numbers:
        base = bases
        alphabet = alphabets

        def __init__(self, num):
            self.value = num
            print((self.value, self.base, self.alphabet))

        def __add__(self, other):
            a = decimal(self.value, self.alphabet, self.base)
            b = decimal(other.value, other.alphabet, self.base)
            print((a, b))
            return numbers(to_base(a + b, self.base, self.alphabet))

        def __sub__(self, other):
            a = decimal(self.value, self.alphabet, self.base)
            b = decimal(other.value, other.alphabet, self.base)
            return numbers(to_base(a - b, self.base, self.alphabet))

        def __mul__(self, other):
            a = decimal(self.value, self.alphabet, self.base)
            b = decimal(other.value, other.alphabet, self.base)
            return numbers(to_base(a * b, self.base, self.alphabet))

        def __floordiv__(self, other):
            a = decimal(self.value, self.alphabet, self.base)
            b = decimal(other.value, other.alphabet, self.base)
            return numbers(to_base(a // b, self.base, self.alphabet))

        def __str__(self):
            return str(self.value)

        def convert_to(self, other):
            num = decimal(self.value, self.alphabet, self.base)
            num = to_base(num, other.base, other.alphabet)
            print(num)
            return numbers(num)
    return numbers


def to_base(num, base, alphabet):
    conv = []
    num = int(num)
    while num >= base:
        conv.append(alphabet[num % base])
        num = num // base
    conv.append(alphabet[num])
    conv.reverse()
    return ''.join([str(i) for i in conv])


def decimal(num, alphabet, base):
    dec = list(num)
    new = list(range(0, len(alphabet)))
    for i in new:
        for x in range(0, len(dec)):
            if dec[x] == alphabet[i]:
                dec[x] = i
    print(dec)
    dec.reverse()
    decimal = 0
    for (i, n) in enumerate(dec):
        decimal += n * base ** i
    print(decimal)
    return decimal
