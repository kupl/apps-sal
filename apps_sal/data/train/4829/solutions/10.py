def compose(*func):
    return C(func)
    
class C:
    def __init__(self,func):
        self.func = list(func)[::-1]
        
    def __call__(self,*value):
        value = sum(value)  
        for f in self.func:
            value = f(value)
        return value
