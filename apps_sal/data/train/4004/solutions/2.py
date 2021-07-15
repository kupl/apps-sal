from collections import Counter, OrderedDict

class OC(Counter,OrderedDict): pass

def first_dup(s):
    return next((c for c,n in OC(s).items() if n>1), None)
