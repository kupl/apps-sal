def handle(func, success, failure, *exceptions):
    class manager:
        def __enter__(self):
            pass
        def __exit__(self, type, value, traceback):
            if isinstance(value, exceptions):
                failure(func, value)
                return True
            return not value
    with manager():
        success(func, func())

