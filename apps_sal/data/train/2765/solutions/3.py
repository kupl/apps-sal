tagname = __import__("re").compile(r"(^|(?<=\s))[^#\.*]").findall

def compare(a, b):
    return max(b, a, key=lambda x: (x.count('#'), x.count('.'), len(tagname(x))))
