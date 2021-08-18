import sys

calls = 0
orig_func = ''


def profiler(frame, event, arg):
    nonlocal calls
    if event == 'call':
        if frame.f_code.co_name != orig_func:
            calls += 1

    return profiler


def count_calls(func, *args, **kwargs):
    """Count calls in function func"""
    nonlocal orig_func
    nonlocal calls
    sys.settrace(profiler)
    orig_func = func

    rv = func(*args, **kwargs)
    count = calls - 1

    # Clean up
    sys.settrace(None)
    calls = 0
    orig_func = ''

    return count, rv
