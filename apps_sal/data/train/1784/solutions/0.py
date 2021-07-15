class CurryPartial:
    def __init__(self, func, *args):
        self.func = func
        self.args = args
    
    def __call__(self, *args):
        return CurryPartial(self.func, *(self.args + args))
    
    def __eq__(self, other):
        try:
            return self.func(*self.args) == other
        except TypeError:
            return CurryPartial(self.func, *self.args[:-1]) == other

def curry_partial(f,*initial_args):
  "Curries and partially applies the initial arguments to the function"
  return CurryPartial(f, *initial_args)
