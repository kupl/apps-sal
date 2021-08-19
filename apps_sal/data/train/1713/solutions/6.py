import sys


def count_calls(func, *args, **kwargs):
    """Count calls in function func"""
    calls = 0

    def trace_counter(frame, event, arg):
        nonlocal calls
        if event != 'call':
            return
        calls += 1
    sys.settrace(trace_counter)
    rv = func(*args, **kwargs)
    sys.settrace(None)
    return (calls - 1, rv)
