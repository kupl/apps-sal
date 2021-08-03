def handle(func, success, failure, *exceptions):
    class CatchError(object):
        def __enter__(self): return None

        def __exit__(self, e_type, *_):
            if e_type is not None and isinstance(e_type(), exceptions):
                failure(func, e_type())
                return True
    with CatchError():
        success(func, func())
