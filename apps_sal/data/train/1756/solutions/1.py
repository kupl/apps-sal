# Steal some contextlib stuff. Teach it to remember the exception instance.
# 3.5 version used, no 3.7+ ABCs.
class suppress:
    """Context manager to suppress specified exceptions
    After the exception is suppressed, execution proceeds with the next
    statement following the with statement.
         with suppress(FileNotFoundError):
             os.remove(somefile)
         # Execution still resumes here if the file was already removed
    """

    def __init__(self, *exceptions):
        self._exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exctype, excinst, exctb):
        # Unlike isinstance and issubclass, CPython exception handling
        # currently only looks at the concrete type hierarchy (ignoring
        # the instance and subclass checking hooks). While Guido considers
        # that a bug rather than a feature, it's a fairly hard one to fix
        # due to various internal implementation details. suppress provides
        # the simpler issubclass based semantics, rather than trying to
        # exactly reproduce the limitations of the CPython interpreter.
        #
        # See http://bugs.python.org/issue12029 for more details
        self.excinst = excinst
        return exctype is not None and issubclass(exctype, self._exceptions)


def handle(func, success, failure, *args):
    result = None  # function result, if any
    ei = None  # exception instance, if any

    for exc in args:  # let's see if we can get any exception
        with suppress(*args):  # muffle everything which we must handle
            scm = suppress(exc)  # get an object here for furter extraction of the instance
            with scm:
                # either this fails for currently tested exception, or some other supported one
                result = func()
                break  # no need to continue if we're good
            if result is None:  # this means we have found our exception
                ei = scm.excinst  # grab the saved guts
                break  # nothing more to do here
        continue  # if we're here, then we have an exception but didn't find which one yet

    if result is not None:  # we got something good, call success as needed
        success(func, result)
        return  # all done, happy hour time

    if ei:  # found that bastard instance
        failure(func, ei)
