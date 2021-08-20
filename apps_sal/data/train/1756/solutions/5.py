class Handler:

    def __init__(self, func, success, failure, *exception_types):
        self.func = func
        self.success = success
        self.failure = failure
        self.exception_types = exception_types

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if isinstance(exc_value, self.exception_types):
            self.failure(self.func, exc_value)
            return True


def handle(func, success, failure, *exception_types):
    with Handler(func, success, failure, *exception_types):
        success(func, func())
