class suppress:
    """Context manager to suppress specified exceptions
    After the exception is suppressed, execution proceeds with the next
    statement following the with statement.
         with suppress(FileNotFoundError):
             os.remove(somefile)
    """

    def __init__(self, *exceptions):
        self._exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exctype, excinst, exctb):
        self.excinst = excinst
        return exctype is not None and issubclass(exctype, self._exceptions)


def handle(func, success, failure, *args):
    result = None
    ei = None

    for exc in args:
        with suppress(*args):
            scm = suppress(exc)
            with scm:
                result = func()
                break
            if result is None:
                ei = scm.excinst
                break
        continue

    if result is not None:
        success(func, result)
        return

    if ei:
        failure(func, ei)
