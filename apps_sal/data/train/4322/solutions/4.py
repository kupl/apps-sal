check = __import__('re').compile('(?:[A-Z]\\d){5}\\.\\-[A-Z]\\%\\d\\.\\d\\d\\.').search


def body_count(code):
    return bool(check(code))
