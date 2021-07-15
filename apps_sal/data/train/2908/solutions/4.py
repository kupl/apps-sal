def flatten(dct):
    
    def extract(dct):
        for k,v in dct.items():
            stk.append(k)
            if isinstance(v,dict) and v: yield from extract(v)
            else:                        yield ('/'.join(stk), v or '')
            stk.pop()
    
    stk = []
    return dict(extract(dct))
