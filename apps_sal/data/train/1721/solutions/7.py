import copy
class NumClass:
    def __init__(self, alphabet):
        self.base = len(alphabet)
        self.alphabet = alphabet

    def set_value_str(self, value):
        self.str_value = value
        self.int_value = 0
        for c in value:
            self.int_value = self.int_value * self.base
            self.int_value += self.alphabet.index(c)
    
    def set_value_int(self, value):
        self.int_value = value
        self.str_value = ''
        while value > 0:
            self.str_value = self.alphabet[value % self.base] + self.str_value
            value = value // self.base
        if len(self.str_value) == 0:
            self.str_value = self.alphabet[0]
    def __str__(self):
        return self.str_value

def create_number_class(alphabet):
    def __init__(self, value = None):
        NumClass.__init__(self, alphabet)
        if value != None:
            self.set_value_str(value)
        else:
            self.set_value_int(0)
    
    def __add__(self, other):
        result = copy.deepcopy(self)
        result.set_value_int(self.int_value + other.int_value)
        return result
    
    def __sub__(self, other):
        result = copy.deepcopy(self)
        result.set_value_int(self.int_value - other.int_value)
        return result

    def __mul__(self, other):
        result = copy.deepcopy(self)
        result.set_value_int(self.int_value * other.int_value)
        return result

    def __floordiv__(self, other):
        result = copy.deepcopy(self)
        result.set_value_int(self.int_value // other.int_value)
        return result
    
    def convert_to(self, convert_type):
        ret = convert_type()
        ret.set_value_int(self.int_value)
        return ret

    newclass = type('NumClass' + str(len(alphabet)), (NumClass, ), 
    {"__init__":__init__, "__add__":__add__, "__sub__":__sub__, "__mul__":__mul__, "__floordiv__":__floordiv__, "convert_to":convert_to})
    return newclass
