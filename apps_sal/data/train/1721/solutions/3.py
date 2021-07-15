def create_number_class(alp):
    alphabet = {j: i for i, j in enumerate(alp)}
    class BinClass:
        def __init__(self, text) : self.text = text
        __add__ = lambda self, other:self.op(self.text,other.text,'+')
        __sub__ = lambda self, other:self.op(self.text,other.text,'-')
        __mul__ = lambda self, other:self.op(self.text,other.text,'*')
        __floordiv__ = lambda self, other:self.op(self.text,other.text,'//')
        __str__ = lambda self:self.text  
        
        op = lambda self,a,b,sign:BinClass(self.from_decimal(eval('{} {} {}'.format(self.to_decimal(a),sign,self.to_decimal(b)))) or alp[0])
        convert_to = lambda self, base:base(self.text).from_decimal(self.to_decimal(self.text))
        to_decimal = lambda self, s:sum(alphabet[j] * (len(alp) ** (len(s)-1 - i)) for i, j in enumerate(s))
        from_decimal = lambda self,s ,li=[]:self.from_decimal(s//len(alp),li+[s%len(alp)]) if s else ''.join([alp[int(i)] for i in li[::-1]])
    return BinClass 
