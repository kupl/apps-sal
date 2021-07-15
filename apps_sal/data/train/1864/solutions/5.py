import itertools

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:          
        expression = \"{{{0}}}\".format(expression)
        s = []
        exp = ''        
        for x in (expression):
            if x in ('{', ',', '}'):
                if exp:
                    s.append([exp])
                    exp = ''
                
                while len(s) > 2 and s[-1] not in ('{', ',', '}') and s[-2] not in ('{', ',', '}'):
                    w2, w1 = s.pop(), s.pop()
                    s.append(sorted([''.join(y) for y in itertools.product(w1,w2)]))                                                                     
                
                if x == \"}\":
                    words = set()
                    w = s.pop()                        
                    while w != '{':
                        if w != \",\":                          
                            words.update(w)
                            
                        w = s.pop()
                        
                    s.append(sorted(words))
                else:
                    s.append(x)  
                    
            else:
                if exp == '':
                    exp = x
                else:
                    exp += x
                    
        return s[0]

