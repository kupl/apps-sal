import sys


def count_calls(func, *args, **kwargs):
    """Count calls in function func"""
    def tracefunc(frame, event, arg):
        nonlocal calls
        if event == "call":
            calls += 1
        return tracefunc

    calls = -1
    sys.settrace(tracefunc)
    rv = func(*args, **kwargs)
    return calls, rv
