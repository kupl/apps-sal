import sys


def count_calls(func, *args, **kwargs):
    """Count calls in function func"""
    tracer = Tracer()
    sys.settrace(tracer.my_tracer)
    rv = func(*args, **kwargs)
    return tracer.count, rv


class Tracer:
    count: int = -1

    def my_tracer(self, frame, event, arg=None):
        if event == 'call':
            self.count += 1
        return self.my_tracer
