import contextlib


def handle(func, success, failure, *exceptions):
    with contextlib.suppress(*exceptions):
        return success(func, func())
    return failure(func, ZeroDivisionError())
