class HandleException:
    def __init__(self, func, failure, exceptions):
        self.target = func
        self.failure = failure
        self.captures = exceptions

    def __enter__(self):
        pass
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None and issubclass(exc_type, self.captures):
            self.failure(self.target, exc_value)
            return True


def handle(func, success, failure, *exceptions):
    with HandleException(func, failure, exceptions):
        return success(func, func())
