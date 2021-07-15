import sys

def count_calls(func, *args, **kwargs):

    def handler(_,line,k):
        handler.count += int(line=='call')
        
    handler.__dict__['count'] = 0
    sys.settrace(handler)
    
    rv = func(*args, **kwargs)
    return handler.count - 1, rv
