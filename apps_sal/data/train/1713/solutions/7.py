def count_calls(func, *args, **kwargs):
    """Count calls in function func"""
    calls = 0
    d = {'calls': 0}
    import sys
    def tracefunc(frame, event, arg):
        if event=='call':           
            d['calls'] +=  1
    sys.settrace(tracefunc)
    rv = func(*args, **kwargs)
    calls = d['calls'] - 1
    return calls, rv


