from contextlib import ContextDecorator


class Swallower:

    def __init__(self, exns):
        self.exns = exns

    def __enter__(self):
        return self

    def __exit__(self, kls, val, trace):
        if not val:
            self.fail = None
            return True
        elif any((isinstance(val, e) for e in self.exns)):
            self.fail = val
            return True
        else:
            return False


def handle(func, success, failure, *exceptions):
    swallower = Swallower(exceptions)
    with swallower:
        val = func()
    if swallower.fail:
        failure(func, swallower.fail)
    else:
        success(func, val)
