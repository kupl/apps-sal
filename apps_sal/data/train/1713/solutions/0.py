import sys


def count_calls(func, *args, **kwargs):
    """Count calls in function func"""

    calls = [-1]

    def tracer(frame, event, arg):
        if event == 'call':
            calls[0] += 1
        return tracer
    sys.settrace(tracer)

    rv = func(*args, **kwargs)

    return calls[0], rv
