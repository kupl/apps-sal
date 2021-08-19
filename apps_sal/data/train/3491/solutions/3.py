REGEX = __import__('re').compile('((.)\\2*)(?=((.)\\4*(?:\\2|\\4)*))').findall


def substring(strng):
    if len(set(strng)) <= 2:
        return strng
    return max((x + y for (x, _, y, _) in REGEX(strng)), key=len)
