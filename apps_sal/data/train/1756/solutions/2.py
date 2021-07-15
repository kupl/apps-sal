from contextlib import suppress

def handle(func, success, failure, *exceptions):
    class silenced:
        def __enter__(self): return self
        def __exit__(self, type, value, traceback):
            nonlocal ret
            if not type: success(func, ret)
            if isinstance(value, exceptions): failure(func, value)
            
    with suppress(*exceptions), silenced():
        ret = func()
