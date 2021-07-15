import sys


def count_calls(func, *args, **kwargs):
    """Count calls in function func"""
    tracer = Tracer(func)
    sys.settrace(tracer.my_tracer)
    rv = func(*args, **kwargs)
    return tracer.count, rv


class Tracer:
    count: int = 0
    func_name: str
    recursive: bool = False

    def __init__(self, func: callable):
        self.func_name = func.__name__

    def my_tracer(self, frame, event, arg=None):
        func_name = frame.f_code.co_name
        if event == 'call' and (self.recursive or func_name != self.func_name):
            self.count += 1
        elif func_name == self.func_name and not self.recursive:
            self.recursive = True
        return self.my_tracer
