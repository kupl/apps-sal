def array(string):
    r = ' '.join(string.split(',')[1:-1]) 
    return r if len(r)>0 else None
    

