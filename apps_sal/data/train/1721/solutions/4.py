def create_number_class(alphabet):
    jinwei = len(alphabet)

    def str2dec(string: str) -> int:
        (dec, base) = (0, 1)
        for dig in reversed(string):
            dec += base * alphabet.index(dig)
            base *= jinwei
        return dec

    def dec2str(dec: int) -> str:
        string = ''
        while 1:
            string += alphabet[dec % jinwei]
            dec = dec // jinwei
            if 0 is dec:
                return string[::-1]

    class number:

        def __init__(self, str_or_dec):
            if isinstance(str_or_dec, str):
                self.str = str_or_dec
                self.dec = str2dec(self.str)
            else:
                self.dec = str_or_dec
                self.str = dec2str(self.dec)

        def convert_to(self, _class):
            return _class(self.dec)

        def __str__(self):
            return self.str

        def __add__(self, x):
            return number(self.dec + x.dec)

        def __sub__(self, x):
            return number(self.dec - x.dec)

        def __mul__(self, x):
            return number(self.dec * x.dec)

        def __floordiv__(self, x):
            return number(self.dec // x.dec)
    return number
