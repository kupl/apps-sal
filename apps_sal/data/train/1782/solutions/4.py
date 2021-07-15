import re
class Simplexer(object):

    def __init__(self, expression):
        r,finded = [],[]
        pattern = [(r'\d+','integer'),(r'\btrue\b|\bfalse\b','boolean'),(r'".*"','string'),(r'[-+*/%().=]','operator'),(r'if|else|for|while|return|func|break','keyword'),(r'\s+','whitespace'),(r'[a-zA-Z0-9_$]+','identifier')]
        def do(a,b,s=0):
            for i in re.finditer(a, expression):
                r1 = not any(k<=i.start()<=l for k,l in finded)
                if (s and not i.group()[0].isdigit() and r1) or r1:
                    finded.append([i.start(),i.end()-1])
                    r.append([i.group(), i.start(), b])
        for i,j in pattern : do(i,j,0 if j!='identifier' else 1)
        self.r = [Token(i[0], i[2]) for i in sorted(r, key=lambda x: x[1])]
        self.l,self.n = len(self.r),-1
    def __iter__(self): 
        return self

    def __next__(self):
        try:
            self.n += 1
            return self.r[self.n]
        except IndexError : raise StopIteration
