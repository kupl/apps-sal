class ErrorHandler:

    def __init__(self, *exceptions):
        self._exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exctype, excinst, exctb):
        self.traceback = exctype
        return exctype and issubclass(exctype, self._exceptions)


def handle(func, success, failure, *exceptions):
    handler = ErrorHandler(*exceptions)
    with handler:
        return success(func, func())
    return failure(func, handler.traceback())
