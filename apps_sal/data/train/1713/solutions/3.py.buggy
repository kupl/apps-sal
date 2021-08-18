import sys

calls = 0


def trace(frame, event, arg):
    nonlocal calls
    if event == 'call':
        calls += 1


sys.settrace(trace)


def count_calls(func, *args, **kwargs):
    nonlocal calls
    calls = -1
    result = func(*args, **kwargs)
    return calls, result
