from collections import Iterable

def unpack(l):    
    return [l] if not isinstance(l, Iterable) or type(l) == str else unpack(l.items()) if type(l) == dict else [e for a in [unpack(e) for e in l] for e in a]
